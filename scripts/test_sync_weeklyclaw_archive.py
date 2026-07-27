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
    def test_refresh_youtube_cards_preserves_episode_20_thumbnail_override(self):
        videos = {
            20: {
                "id": "MSRFmpDfaTg",
                "url": "https://www.youtube.com/watch?v=MSRFmpDfaTg",
                "thumbnail": "https://i.ytimg.com/vi/MSRFmpDfaTg/maxresdefault.jpg",
            }
        }
        archive_html = """
        <article class="week-card" data-kind="main">
          <div class="thumb"><img src="/old.jpg"><span class="week-number">W20</span><span class="availability">Main slides</span></div>
          <p class="card-kicker">Main slides</p>
          <div class="card-actions"><button>Slides</button></div>
        </article>
        """
        homepage_html = """
        <article class="episode-card">
          <div class="episode-thumb"><img src="old.jpg"><span class="episode-week">W20</span></div>
          <p class="packet-label">Main slides</p>
          <div class="episode-actions"><a>Slides</a></div>
        </article>
        """

        refreshed_archive = SYNC.refresh_youtube_cards(archive_html, videos, archive=True)
        refreshed_homepage = SYNC.refresh_youtube_cards(homepage_html, videos, archive=False)

        expected = "assets/youtube-thumbnails/w20-v2-ai-got-cheap-approved-20260727.jpg"
        self.assertIn(f'/{expected}', refreshed_archive)
        self.assertIn(expected, refreshed_homepage)
        self.assertNotIn("assets/youtube-thumbnails/w20.jpg", refreshed_archive)
        self.assertNotIn("assets/youtube-thumbnails/w20.jpg", refreshed_homepage)

    def test_refresh_youtube_cards_preserves_episode_21_thumbnail_override(self):
        videos = {
            21: {
                "id": "dquJyEBQWpE",
                "url": "https://www.youtube.com/watch?v=dquJyEBQWpE",
                "thumbnail": "https://i.ytimg.com/vi/dquJyEBQWpE/maxresdefault.jpg",
            }
        }
        archive_html = """
        <article class="week-card" data-kind="main">
          <div class="thumb"><img src="/old.jpg"><span class="week-number">W21</span><span class="availability">Main slides</span></div>
          <p class="card-kicker">Main slides</p>
          <div class="card-actions"><button>Slides</button></div>
        </article>
        """
        homepage_html = """
        <article class="episode-card">
          <div class="episode-thumb"><img src="old.jpg"><span class="episode-week">W21</span></div>
          <p class="packet-label">Main slides</p>
          <div class="episode-actions"><a>Slides</a></div>
        </article>
        """

        refreshed_archive = SYNC.refresh_youtube_cards(archive_html, videos, archive=True)
        refreshed_homepage = SYNC.refresh_youtube_cards(homepage_html, videos, archive=False)

        expected = "assets/youtube-thumbnails/w21-v2-approved-20260727.jpg"
        self.assertIn(f'/{expected}', refreshed_archive)
        self.assertIn(expected, refreshed_homepage)
        self.assertNotIn("assets/youtube-thumbnails/w21.jpg", refreshed_archive)
        self.assertNotIn("assets/youtube-thumbnails/w21.jpg", refreshed_homepage)

    def test_refresh_youtube_cards_preserves_episode_22_thumbnail_override(self):
        videos = {
            22: {
                "id": "f2yugYwXOBo",
                "url": "https://www.youtube.com/watch?v=f2yugYwXOBo",
                "thumbnail": "https://i.ytimg.com/vi/f2yugYwXOBo/maxresdefault.jpg",
            }
        }
        archive_html = """
        <article class="week-card" data-kind="main">
          <div class="thumb"><img src="/old.jpg"><span class="week-number">W22</span><span class="availability">Main slides</span></div>
          <p class="card-kicker">Main slides</p>
          <div class="card-actions"><button>Slides</button></div>
        </article>
        """
        homepage_html = """
        <article class="episode-card">
          <div class="episode-thumb"><img src="old.jpg"><span class="episode-week">W22</span></div>
          <p class="packet-label">Main slides</p>
          <div class="episode-actions"><a>Slides</a></div>
        </article>
        """

        refreshed_archive = SYNC.refresh_youtube_cards(archive_html, videos, archive=True)
        refreshed_homepage = SYNC.refresh_youtube_cards(homepage_html, videos, archive=False)

        expected = "assets/youtube-thumbnails/w22-v2-the-sandbox-failed-approved-20260727.jpg"
        self.assertIn(f'/{expected}', refreshed_archive)
        self.assertIn(expected, refreshed_homepage)
        self.assertNotIn("assets/youtube-thumbnails/w22.jpg", refreshed_archive)
        self.assertNotIn("assets/youtube-thumbnails/w22.jpg", refreshed_homepage)

    def test_refresh_youtube_cards_wires_archive_media_to_in_page_player(self):
        videos = {
            22: {
                "id": "f2yugYwXOBo",
                "url": "https://www.youtube.com/watch?v=f2yugYwXOBo",
                "thumbnail": "https://i.ytimg.com/vi/f2yugYwXOBo/maxresdefault.jpg",
            }
        }
        archive_html = """
        <article class="week-card" data-kind="main">
          <div class="thumb"><img src="/old.jpg"><span class="week-number">W22</span><span class="availability">Main slides</span></div>
          <p class="card-kicker">Main slides</p>
          <div class="card-actions"><button>Slides</button></div>
        </article>
        """

        refreshed = SYNC.refresh_youtube_cards(archive_html, videos, archive=True)

        self.assertIn('data-week="22"', refreshed)
        self.assertIn('data-video-id="f2yugYwXOBo"', refreshed)
        self.assertIn('href="https://www.youtube.com/watch?v=f2yugYwXOBo" data-play-video="22"', refreshed)
        self.assertIn('aria-label="Play Weekly Claw episode 22 video on this page"', refreshed)
        self.assertNotIn('target="_blank"', refreshed)
        self.assertEqual(SYNC.refresh_youtube_cards(refreshed, videos, archive=True), refreshed)

    def test_offline_sync_preserves_latest_archive_player_wiring(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            episode = repo / "episodes" / "22"
            episode.mkdir(parents=True)
            (episode / "deck.html").write_text("fixture")
            (repo / "episodes" / "index.html").write_text(
                """
                <div class="fact"><strong>01</strong><span>archived episodes</span></div>
                <div class="gallery" id="gallery">
                  <article class="week-card" data-kind="main" data-week="22" data-video-id="f2yugYwXOBo" data-audio-src="/audio/weekly-claw-22.mp3">
                    <a class="thumb youtube-thumb" href="https://www.youtube.com/watch?v=f2yugYwXOBo" data-play-video="22">
                      <span class="week-number">W22</span>
                    </a>
                    <div class="card-copy"><p class="card-kicker">Video · main slides</p><h3>Existing episode</h3><p>Existing summary.</p></div>
                    <div class="card-actions"><a class="source-link" href="https://www.youtube.com/watch?v=f2yugYwXOBo" data-play-video="22" aria-label="Play Weekly Claw episode 22 video on this page">Video</a></div>
                  </article>
                </div>
                """
            )

            SYNC.update_episodes_index(
                repo,
                22,
                {"headline": "Existing episode", "desc": "Existing summary."},
                {},
            )

            refreshed = (repo / "episodes" / "index.html").read_text()
            self.assertIn('data-video-id="f2yugYwXOBo"', refreshed)
            self.assertIn('data-audio-src="/audio/weekly-claw-22.mp3"', refreshed)
            self.assertIn('href="https://www.youtube.com/watch?v=f2yugYwXOBo" data-play-video="22"', refreshed)

            videos = {
                22: {
                    "id": "f2yugYwXOBo",
                    "url": "https://www.youtube.com/watch?v=f2yugYwXOBo",
                    "thumbnail": "https://i.ytimg.com/vi/f2yugYwXOBo/maxresdefault.jpg",
                }
            }
            SYNC.update_episodes_index(
                repo,
                22,
                {"headline": "Existing episode", "desc": "Existing summary."},
                videos,
            )
            refreshed = (repo / "episodes" / "index.html").read_text()
            self.assertIn('data-audio-src="/audio/weekly-claw-22.mp3"', refreshed)

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
