#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("verify_youtube_channel_gate.py")
EXPECTED = {
    "display": "Weeklyclaw",
    "handle": "@WeeklyClaw",
    "channel_id": "UCa0Mxn9vyx6NnU-aBgRcRvg",
}


def manifest(status: str = "UNLISTED_REVIEW", gate: str = "") -> str:
    return "\n".join(
        (
            "# Weekly Claw test release manifest",
            f"Status: {status}",
            "",
            "## YouTube channel identity gate",
            f"- Intended display name: `{EXPECTED['display']}`",
            f"- Intended handle: `{EXPECTED['handle']}`",
            f"- Intended immutable channel ID: `{EXPECTED['channel_id']}`",
            "- Approved replacement authorization text (required when not the default tuple): `not applicable`",
            "- Approved replacement authorization time and scope: `not applicable`",
            f"- Gate result: `{gate}`" if gate else "- Gate result:",
            "",
        )
    )


class ChannelGateTests(unittest.TestCase):
    def run_gate(self, text: str, phase: str, **observed: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "release-manifest.md"
            path.write_text(text, encoding="utf-8")
            return subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(path),
                    "--phase",
                    phase,
                    "--observed-display-name",
                    observed.get("display", EXPECTED["display"]),
                    "--observed-handle",
                    observed.get("handle", EXPECTED["handle"]),
                    "--observed-channel-id",
                    observed.get("channel_id", EXPECTED["channel_id"]),
                ],
                text=True,
                capture_output=True,
                check=False,
            )

    def test_missing_tuple_blocks_before_file_selection(self) -> None:
        result = self.run_gate("Status: UNLISTED_REVIEW\n", "pre-upload")
        self.assertEqual(result.returncode, 42)
        self.assertIn("incomplete", result.stderr)

    def test_pre_upload_mismatch_blocks(self) -> None:
        result = self.run_gate(manifest(), "pre-upload", handle="@DifferentChannel")
        self.assertEqual(result.returncode, 42)
        self.assertIn("YOUTUBE_CHANNEL_IDENTITY_BLOCKED", result.stderr)

    def test_post_upload_mismatch_blocks(self) -> None:
        result = self.run_gate(manifest(), "post-upload", handle="@DifferentChannel")
        self.assertEqual(result.returncode, 43)
        self.assertIn("WRONG_YOUTUBE_CHANNEL", result.stderr)

    def test_contradictory_public_verified_status_blocks(self) -> None:
        result = self.run_gate(manifest(status="PUBLIC_VERIFIED", gate="WRONG_YOUTUBE_CHANNEL"), "post-upload")
        self.assertEqual(result.returncode, 43)
        self.assertIn("contradicts", result.stderr)

    def test_post_upload_requires_explicit_pass(self) -> None:
        result = self.run_gate(manifest(), "post-upload")
        self.assertEqual(result.returncode, 43)
        self.assertIn("expected 'PASS'", result.stderr)

    def test_duplicate_identity_field_blocks(self) -> None:
        text = manifest(gate="PASS").replace(
            f"- Intended handle: `{EXPECTED['handle']}`",
            f"- Intended handle: `{EXPECTED['handle']}`\n- Intended handle: `{EXPECTED['handle']}`",
        )
        result = self.run_gate(text, "pre-upload")
        self.assertEqual(result.returncode, 42)
        self.assertIn("duplicate identity fields", result.stderr)

    def test_matching_tuple_passes(self) -> None:
        result = self.run_gate(manifest(gate="PASS"), "post-upload")
        self.assertEqual(result.returncode, 0)
        self.assertIn("YOUTUBE_CHANNEL_GATE_PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
