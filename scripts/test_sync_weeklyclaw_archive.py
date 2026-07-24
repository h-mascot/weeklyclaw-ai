import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("sync-weeklyclaw-archive.py")
SPEC = importlib.util.spec_from_file_location("weeklyclaw_sync", MODULE_PATH)
SYNC = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(SYNC)


class SyncMetadataTests(unittest.TestCase):
    def test_generic_deck_title_uses_first_story_frame_and_skips_build_notes(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            episode = repo / "episodes" / "22"
            episode.mkdir(parents=True)
            (episode / "deck.html").write_text(
                """<!doctype html><title>Weekly Claw #22 &mdash; July 24, 2026</title>
                <h1><span>Weekly Claw</span></h1>
                <h2>Six stories. <span>One thread.</span></h2>"""
            )
            (episode / "agenda.md").write_text(
                """# Weekly Claw Episode 22

**Date:** Friday, July 24, 2026 · 4:00 PM ET

> **Build notes:** Internal production notes that must never become site copy.

## Cold Open — The Frame

Welcome back to Weekly Claw. Six stories share one thread: control of context, permissions, and workflow.
"""
            )

            meta = SYNC.deck_meta(repo, 22)

            self.assertEqual(meta["headline"], "Six stories. One thread.")
            self.assertTrue(meta["desc"].startswith("Welcome back to Weekly Claw."))
            self.assertNotIn("Build notes", meta["desc"])

    def test_latest_episode_link_advances_from_any_previous_week(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "index.html").write_text(
                '<div class="latest-action"><a class="button" href="/episodes?week=21&amp;deck=main">Open episode <span>→</span></a></div>'
            )

            SYNC.update_homepage(
                repo,
                22,
                {"headline": "Six stories. One thread.", "date": "Friday, July 24, 2026", "desc": "Episode summary."},
                {},
            )

            html = (repo / "index.html").read_text()
            self.assertIn('/episodes?week=22&amp;deck=main">Open episode', html)
            self.assertNotIn('/episodes?week=21&amp;deck=main">Open episode', html)

    def test_public_episode_paths_exclude_internal_research_notes(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            episode = repo / "episodes" / "22"
            (episode / "agenda").mkdir(parents=True)
            (episode / "source-assets").mkdir()
            for relative in [
                "deck.html",
                "agenda.md",
                "agenda/index.html",
                "source-assets/visual.jpg",
                "daily-topic-list.md",
                "henry-talking-points.md",
            ]:
                path = episode / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("fixture")

            paths = {path.relative_to(repo).as_posix() for path in SYNC.public_episode_paths(repo, 22)}

            self.assertIn("episodes/22/deck.html", paths)
            self.assertIn("episodes/22/agenda/index.html", paths)
            self.assertIn("episodes/22/source-assets", paths)
            self.assertNotIn("episodes/22/daily-topic-list.md", paths)
            self.assertNotIn("episodes/22/henry-talking-points.md", paths)


if __name__ == "__main__":
    unittest.main()
