#!/usr/bin/env python3
"""Fail-closed verifier for the Weekly Claw YouTube channel gate."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_TUPLE = (
    "Weeklyclaw",
    "@WeeklyClaw",
    "UCa0Mxn9vyx6NnU-aBgRcRvg",
)
PRE_BLOCKED = 42
POST_BLOCKED = 43
IDENTITY_KEYS = {
    "Intended display name",
    "Intended handle",
    "Intended immutable channel ID",
    "Approved replacement authorization text (required when not the default tuple)",
    "Approved replacement authorization time and scope",
    "Pre-upload Studio channel readback (display name / handle / channel ID / time)",
    "Post-upload Studio channel readback (display name / handle / channel ID / time)",
    "Post-upload watch-page channel readback (display name / handle / channel ID / time)",
    "Gate result",
}


def clean(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == "`":
        return value[1:-1]
    return value


def read_manifest(path: Path) -> tuple[dict[str, str], str, list[str]]:
    fields: dict[str, str] = {}
    duplicates: list[str] = []
    status = ""
    for line in path.read_text(encoding="utf-8").splitlines():
        status_match = re.match(r"^Status:\s*(.*)$", line)
        if status_match:
            status = clean(status_match.group(1)).split(" — ", 1)[0].strip()
        field_match = re.match(r"^- ([^:]+):\s*(.*)$", line)
        if field_match:
            key = field_match.group(1).strip()
            if key in fields and key in IDENTITY_KEYS:
                duplicates.append(key)
            fields[key] = clean(field_match.group(2))
    return fields, status, duplicates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--phase", choices=("pre-upload", "post-upload"), required=True)
    parser.add_argument("--observed-display-name", required=True)
    parser.add_argument("--observed-handle", required=True)
    parser.add_argument("--observed-channel-id", required=True)
    args = parser.parse_args()

    if not args.manifest.is_file():
        print(f"YOUTUBE_CHANNEL_IDENTITY_BLOCKED: manifest missing: {args.manifest}", file=sys.stderr)
        return PRE_BLOCKED

    fields, status, duplicates = read_manifest(args.manifest)
    if duplicates:
        print(f"YOUTUBE_CHANNEL_IDENTITY_BLOCKED: duplicate identity fields: {sorted(set(duplicates))}", file=sys.stderr)
        return PRE_BLOCKED
    intended = (
        fields.get("Intended display name", ""),
        fields.get("Intended handle", ""),
        fields.get("Intended immutable channel ID", ""),
    )
    if any(not value for value in intended):
        print("YOUTUBE_CHANNEL_IDENTITY_BLOCKED: intended channel tuple is incomplete", file=sys.stderr)
        return PRE_BLOCKED

    if intended != DEFAULT_TUPLE:
        approval = fields.get(
            "Approved replacement authorization text (required when not the default tuple)", ""
        )
        approval_time_scope = fields.get("Approved replacement authorization time and scope", "")
        if not approval or approval.lower() in {"pending", "none", "not applicable", "n/a"}:
            print("YOUTUBE_CHANNEL_IDENTITY_BLOCKED: non-default tuple lacks approval text", file=sys.stderr)
            return PRE_BLOCKED
        if not approval_time_scope or approval_time_scope.lower() in {"pending", "none", "not applicable", "n/a"}:
            print("YOUTUBE_CHANNEL_IDENTITY_BLOCKED: non-default tuple lacks approval time and scope", file=sys.stderr)
            return PRE_BLOCKED

    gate = fields.get("Gate result", "")
    if status == "PUBLIC_VERIFIED" and gate != "PASS":
        print("WRONG_YOUTUBE_CHANNEL: PUBLIC_VERIFIED contradicts the channel gate result", file=sys.stderr)
        return POST_BLOCKED

    observed = (
        args.observed_display_name,
        args.observed_handle,
        args.observed_channel_id,
    )
    if observed != intended:
        code = PRE_BLOCKED if args.phase == "pre-upload" else POST_BLOCKED
        label = "YOUTUBE_CHANNEL_IDENTITY_BLOCKED" if args.phase == "pre-upload" else "WRONG_YOUTUBE_CHANNEL"
        print(f"{label}: expected {intended!r}, observed {observed!r}", file=sys.stderr)
        return code

    if args.phase == "post-upload" and gate != "PASS":
        print(f"WRONG_YOUTUBE_CHANNEL: post-upload manifest gate result is {gate!r}, expected 'PASS'", file=sys.stderr)
        return POST_BLOCKED

    print("YOUTUBE_CHANNEL_GATE_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
