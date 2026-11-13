#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import statistics
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def tool(name: str) -> str:
    found = shutil.which(name)
    if found:
        return found
    fallback = Path("/opt/homebrew/bin") / name
    if fallback.is_file():
        return str(fallback)
    raise FileNotFoundError(f"{name} not found")


def probe(path: Path) -> dict:
    completed = subprocess.run(
        [
            tool("ffprobe"),
            "-v",
            "error",
            "-show_entries",
            "format=duration,size,bit_rate:stream=index,codec_type,codec_name,profile,width,height,"
            "pix_fmt,r_frame_rate,avg_frame_rate,sample_aspect_ratio,display_aspect_ratio,"
            "color_space,color_transfer,color_primaries,sample_rate,channels,channel_layout,"
            "start_time,duration,bit_rate",
            "-of",
            "json",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def video_stream(data: dict) -> dict:
    return next(stream for stream in data["streams"] if stream["codec_type"] == "video")


def audio_stream(data: dict) -> dict:
    return next(stream for stream in data["streams"] if stream["codec_type"] == "audio")


def frame_timing(path: Path) -> dict:
    completed = subprocess.run(
        [
            tool("ffprobe"),
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "packet=pts_time,duration_time",
            "-of",
            "csv=p=0",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    packets: list[tuple[float, float]] = []
    for line in completed.stdout.splitlines():
        fields = line.split(",")
        if len(fields) != 2 or "N/A" in fields:
            continue
        packets.append((float(fields[0]), float(fields[1])))
    if not packets:
        return {"packet_count": 0, "constant": False}
    durations = [duration for _, duration in packets]
    nominal = statistics.median(durations)
    tolerance = max(0.000001, nominal * 0.001)
    duration_outliers = sum(abs(value - nominal) > tolerance for value in durations)
    ordered_pts = sorted(pts for pts, _ in packets)
    timestamp_outliers = sum(
        abs(current - previous - nominal) > tolerance
        for previous, current in zip(ordered_pts, ordered_pts[1:])
    )
    return {
        "packet_count": len(durations),
        "nominal_duration": nominal,
        "video_span": max(pts + packet_duration for pts, packet_duration in packets)
        - min(pts for pts, _ in packets),
        "duration_outliers": duration_outliers,
        "timestamp_outliers": timestamp_outliers,
        "constant": duration_outliers == 0 and timestamp_outliers == 0,
    }


def stream_hash(path: Path) -> str:
    command = [
        tool("ffmpeg"),
        "-v",
        "error",
        "-i",
        str(path),
        "-map",
        "0:v:0",
        "-c",
        "copy",
        "-bsf:v",
        "h264_mp4toannexb",
        "-f",
        "h264",
        "-",
    ]
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
    )
    if process.stdout is None:
        raise RuntimeError("ffmpeg video stream pipe was not created")
    digest = hashlib.sha256()
    while chunk := process.stdout.read(1024 * 1024):
        digest.update(chunk)
    if process.wait() != 0:
        raise subprocess.CalledProcessError(process.returncode, process.args)
    return digest.hexdigest()


def full_decode(path: Path) -> None:
    subprocess.run(
        [
            tool("ffmpeg"),
            "-v",
            "error",
            "-xerror",
            "-i",
            str(path),
            "-map",
            "0:v",
            "-map",
            "0:a",
            "-f",
            "null",
            "-",
        ],
        check=True,
    )


def loudness(path: Path) -> dict:
    completed = subprocess.run(
        [
            tool("ffmpeg"),
            "-hide_banner",
            "-nostats",
            "-i",
            str(path),
            "-map",
            "0:a:0",
            "-filter:a",
            "ebur128=peak=true",
            "-f",
            "null",
            "-",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    integrated_matches = re.findall(
        r"Integrated loudness:\s*\n\s*I:\s*(-?inf|-?\d+(?:\.\d+)?) LUFS",
        completed.stderr,
    )
    peak_matches = re.findall(
        r"True peak:\s*\n\s*Peak:\s*(-?inf|-?\d+(?:\.\d+)?) dBFS",
        completed.stderr,
    )
    if not integrated_matches or not peak_matches:
        raise RuntimeError("ffmpeg did not report EBU R128 loudness")
    return {
        "integrated_lufs": float(integrated_matches[-1]),
        "true_peak_dbtp": float(peak_matches[-1]),
    }


def file_sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def precise_true_peak(path: Path, sample_rate: int) -> dict:
    """Measure decoded encoded-audio peaks at 8x rate; never use rounded ebur128 for a strict gate."""
    rate = sample_rate * 8
    result = subprocess.run([
        tool("ffmpeg"), "-hide_banner", "-nostats", "-i", str(path),
        "-map", "0:a:0", "-af",
        f"aresample={rate}:resampler=soxr:precision=33,aformat=sample_fmts=dbl,astats=metadata=0:reset=0",
        "-f", "null", "-"], check=True, capture_output=True, text=True)
    peaks = re.findall(r"Peak level dB:\s*(-?inf|-?\d+(?:\.\d+)?)", result.stderr)
    if not peaks:
        raise RuntimeError("No precise oversampled peak result; strict audio gate remains unverified")
    return {"true_peak_dbtp": max(float(v) for v in peaks),
            "true_peak_method": "decoded final audio, 8x SoX resampling precision=33, float64 astats maximum across channels",
            "true_peak_measurement_rate": rate,
            "true_peak_limitations": "Interpolation-based estimate, not a claim of exact mathematical intersample maximum; keep encoding margin."}


def measured_video_bitrate(path: Path, video: dict, span: float) -> dict:
    try:
        value = int(video.get("bit_rate", 0))
    except (ValueError, TypeError):
        value = 0
    if value > 0:
        return {"bits_per_second": value, "method": "ffprobe video stream bit_rate"}
    if span <= 0:
        raise ValueError("Video duration unavailable for packet-bitrate fallback")
    result = subprocess.run([tool("ffprobe"), "-v", "error", "-select_streams", "v:0",
        "-show_entries", "packet=size", "-of", "csv=p=0", str(path)],
        check=True, capture_output=True, text=True)
    values = [int(line.strip()) for line in result.stdout.splitlines() if line.strip().isdigit()]
    if not values:
        raise ValueError("Video packet bytes unavailable; bitrate remains unknown")
    return {"bits_per_second": sum(values) * 8 / span,
            "method": "sum video packet bytes * 8 / measured video timestamp span", "packet_bytes": sum(values), "span_seconds": span}


def ratio(value: str) -> float:
    return float(Fraction(value))


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a rendered podcast master.")
    parser.add_argument("master", type=Path)
    parser.add_argument("--compare-video", type=Path)
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1080)
    parser.add_argument("--fps", type=float)
    parser.add_argument("--sample-rate", type=int, default=48000)
    parser.add_argument("--channels", type=int)
    parser.add_argument("--duration", type=float)
    parser.add_argument("--duration-tolerance", type=float)
    parser.add_argument("--min-video-bitrate", type=int, default=4_000_000)
    parser.add_argument("--min-lufs", type=float, default=-18.0)
    parser.add_argument("--max-lufs", type=float, default=-12.0)
    parser.add_argument("--max-true-peak", type=float, default=-0.1)
    parser.add_argument("--full-decode", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    if not args.master.is_file():
        parser.error(f"master not found: {args.master}")
    if args.compare_video and not args.compare_video.is_file():
        parser.error(f"comparison video not found: {args.compare_video}")
    media_inputs = {args.master.resolve()}
    if args.compare_video:
        media_inputs.add(args.compare_video.resolve())
    if args.report and args.report.resolve() in media_inputs:
        parser.error("report path must not overwrite a media input")

    data = probe(args.master)
    video = video_stream(data)
    audio = audio_stream(data)
    duration = float(data["format"]["duration"])
    timing = frame_timing(args.master)
    levels = loudness(args.master)
    levels["rounded_ebur128_true_peak_dbtp"] = levels["true_peak_dbtp"]
    levels.update(precise_true_peak(args.master, int(audio["sample_rate"])))
    bitrate = measured_video_bitrate(args.master, video, timing["video_span"])
    frame_duration = timing.get("nominal_duration", 0)
    audio_start = float(audio.get("start_time", "nan"))
    audio_duration = float(audio.get("duration", "nan"))
    audio_tolerance = max(frame_duration, 1024 / int(audio["sample_rate"]))
    checks = {
        "video_stream_count": sum(
            stream["codec_type"] == "video" for stream in data["streams"]
        )
        == 1,
        "audio_stream_count": sum(
            stream["codec_type"] == "audio" for stream in data["streams"]
        )
        == 1,
        "dimensions": [int(video["width"]), int(video["height"])] == [args.width, args.height],
        "codec": video.get("codec_name") == "h264",
        "profile": video.get("profile") == "High",
        "square_pixels": video.get("sample_aspect_ratio") in {None, "1:1"},
        "display_aspect_ratio": video.get("display_aspect_ratio") is None
        or Fraction(video["display_aspect_ratio"].replace(":", "/")) == Fraction(args.width, args.height),
        "constant_frame_rate": timing["constant"],
        "pixel_format": video.get("pix_fmt") == "yuv420p",
        "bt709": all(
            video.get(field) == "bt709"
            for field in ("color_space", "color_transfer", "color_primaries")
        ),
        "video_bitrate": bitrate["bits_per_second"] >= args.min_video_bitrate,
        "sample_rate": int(audio["sample_rate"]) == args.sample_rate,
        "channel_count": int(audio["channels"]) in {1, 2},
        "integrated_loudness": args.min_lufs
        <= levels["integrated_lufs"]
        <= args.max_lufs,
        "true_peak": levels["true_peak_dbtp"] <= args.max_true_peak,
        "audio_span": abs(audio_start) <= audio_tolerance
        and abs(audio_start + audio_duration - duration) <= audio_tolerance,
        "video_span": frame_duration > 0
        and abs(timing["video_span"] - duration) <= frame_duration,
    }
    if args.fps is not None:
        checks["fps"] = abs(ratio(video["avg_frame_rate"]) - args.fps) < 0.001
    if args.channels is not None:
        checks["channels"] = int(audio["channels"]) == args.channels
    if args.duration is not None:
        tolerance = (
            args.duration_tolerance
            if args.duration_tolerance is not None
            else 1 / ratio(video["avg_frame_rate"])
        )
        checks["duration"] = abs(duration - args.duration) <= tolerance

    hashes = {
        "master_video_sha256": stream_hash(args.master)
        if video.get("codec_name") == "h264"
        else None
    }
    if args.compare_video:
        comparison = video_stream(probe(args.compare_video))
        hashes["comparison_video_sha256"] = (
            stream_hash(args.compare_video)
            if comparison.get("codec_name") == "h264"
            else None
        )
        checks["video_stream_unchanged"] = (
            hashes["master_video_sha256"] is not None
            and hashes["comparison_video_sha256"] is not None
            and
            hashes["master_video_sha256"] == hashes["comparison_video_sha256"]
        )

    if args.full_decode:
        full_decode(args.master)
        checks["full_decode"] = True

    report = {
        "master": str(args.master.resolve()),
        "master_sha256": file_sha(args.master),
        "video_bitrate_measurement": bitrate,
        "thresholds": {
            "min_video_bitrate": args.min_video_bitrate,
            "min_lufs": args.min_lufs,
            "max_lufs": args.max_lufs,
            "max_true_peak": args.max_true_peak,
        },
        "format": data["format"],
        "video": video,
        "frame_timing": timing,
        "audio": audio,
        "loudness": levels,
        "hashes": hashes,
        "checks": checks,
        "passed": all(checks.values()),
    }
    rendered = json.dumps(report, indent=2) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered)
    sys.stdout.write(rendered)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
