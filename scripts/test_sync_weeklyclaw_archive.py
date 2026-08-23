import importlib.util
import json
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("sync-weeklyclaw-archive.py")
SPEC = importlib.util.spec_from_file_location("weeklyclaw_sync", MODULE_PATH)
SYNC = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(SYNC)


class SyncMetadataTests(unittest.TestCase):
    def test_fetch_youtube_episodes_infers_unnumbered_long_form_uploads(self):
        playlist = {
            "entries": [
                {"id": "EPISODE0023", "title": "AI Models Break Containment", "duration": 3096},
                {"id": "EPISODE0022", "title": "The Sandbox Failed | Weekly Claw #22", "duration": 2800},
                {"id": "SHORT000001", "title": "A short clip", "duration": 45},
                {"id": "EPISODE0021", "title": "The workflow is the moat", "duration": 2600},
                {"id": "EPISODE0020", "title": "Weekly Claw #20", "duration": 2500},
            ]
        }
        completed = subprocess.CompletedProcess([], 0, stdout=json.dumps(playlist), stderr="")

        with patch.object(SYNC.subprocess, "run", return_value=completed):
            videos = SYNC.fetch_youtube_episodes()

        self.assertEqual(videos[23]["id"], "EPISODE0023")
        self.assertEqual(videos[22]["id"], "EPISODE0022")
        self.assertEqual(videos[21]["id"], "EPISODE0021")
        self.assertEqual(videos[20]["id"], "EPISODE0020")
        self.assertNotIn(24, videos)

    def test_refresh_youtube_cards_writes_spotify_ids(self):
        videos = {22: {"id": "f2yugYwXOBo", "url": "https://www.youtube.com/watch?v=f2yugYwXOBo", "thumbnail": "x"}}
        archive_html = """
        <article class="week-card" data-kind="main">
          <div class="thumb"><img src="/old.jpg"><span class="week-number">W22</span><span class="availability">Main slides</span></div>
          <p class="card-kicker">Main slides</p>
          <div class="card-actions"><button>Slides</button></div>
        </article>
        """
        refreshed = SYNC.refresh_youtube_cards(archive_html, videos, archive=True, spotify={22: "2GywqAyfGJMXafRHRbdIa6"})
        self.assertIn('data-video-id="f2yugYwXOBo" data-spotify-id="2GywqAyfGJMXafRHRbdIa6"', refreshed)

        refreshed_no_spotify = SYNC.refresh_youtube_cards(archive_html, videos, archive=True, spotify=None)
        self.assertNotIn("data-spotify-id", refreshed_no_spotify)

    def test_refresh_youtube_cards_writes_audio_sources(self):
        videos = {22: {"id": "f2yugYwXOBo", "url": "https://www.youtube.com/watch?v=f2yugYwXOBo", "thumbnail": "x"}}
        audio = {22: "https://api.riverside.com/hosting-analytics/media/abc123"}
        archive_html = """
        <article class="week-card" data-kind="main">
          <div class="thumb"><img src="/old.jpg"><span class="week-number">W22</span><span class="availability">Main slides</span></div>
          <p class="card-kicker">Main slides</p>
          <div class="card-actions"><button>Slides</button></div>
        </article>
        """
        refreshed = SYNC.refresh_youtube_cards(archive_html, videos, archive=True, audio=audio)
        self.assertIn('data-video-id="f2yugYwXOBo" data-audio-src="https://api.riverside.com/hosting-analytics/media/abc123"', refreshed)

        refreshed_no_audio = SYNC.refresh_youtube_cards(archive_html, videos, archive=True, audio=None)
        self.assertNotIn("data-audio-src", refreshed_no_audio)

    def test_refresh_youtube_cards_replaces_stale_audio_source(self):
        videos = {22: {"id": "f2yugYwXOBo", "url": "https://www.youtube.com/watch?v=f2yugYwXOBo", "thumbnail": "x"}}
        audio = {22: "https://api.riverside.com/hosting-analytics/media/fresh"}
        archive_html = """
        <article class="week-card" data-kind="main" data-week="22" data-video-id="staleId00000" data-audio-src="https://api.riverside.com/hosting-analytics/media/stale">
          <div class="thumb"><img src="/old.jpg"><span class="week-number">W22</span><span class="availability">Main slides</span></div>
          <p class="card-kicker">Main slides</p>
          <div class="card-actions"><button>Slides</button></div>
        </article>
        """
        refreshed = SYNC.refresh_youtube_cards(archive_html, videos, archive=True, audio=audio)
        self.assertIn('data-audio-src="https://api.riverside.com/hosting-analytics/media/fresh"', refreshed)
        self.assertNotIn("media/stale", refreshed)

    def test_fetch_audio_episodes_parses_rss_enclosures(self):
        rss = """
        <channel><item>
          <title>The Sandbox Failed</title>
          <itunes:episode>22</itunes:episode>
          <enclosure url="https://api.riverside.com/hosting-analytics/media/ep22.mp3" type="audio/mpeg"/>
        </item>
        <item>
          <title>Unnumbered item</title>
          <enclosure url="https://api.riverside.com/hosting-analytics/media/other.mp3" type="audio/mpeg"/>
        </item></channel>
        """
        audio = SYNC.fetch_audio_episodes(rss)
        self.assertEqual(audio, {22: "https://api.riverside.com/hosting-analytics/media/ep22.mp3"})

        self.assertEqual(SYNC.fetch_audio_episodes(""), {})

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

    def test_homepage_sync_removes_obsolete_featured_open_episode_link(self):
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
            self.assertNotIn("Open episode", html)
            self.assertNotIn('class="latest-action"', html)

    def test_homepage_sync_updates_featured_player_video_and_drops_stale_audio(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "index.html").write_text(
                """
                <div class="latest-card" data-video-id="f2yugYwXOBo" data-audio-src="/audio/weekly-claw-22.mp3">
                  <div class="latest-number" aria-hidden="true">22</div>
                  <p class="latest-label">Featured latest episode · Previous date</p>
                  <h2 id="latest-title">Previous episode</h2>
                  <p class="latest-meta">Previous summary.</p>
                  <div class="latest-action"><a class="button" href="/episodes?week=22&amp;deck=main">Open episode <span>→</span></a></div>
                </div>
                """
            )
            videos = {
                23: {
                    "id": "ABCDEFGHIJK",
                    "url": "https://www.youtube.com/watch?v=ABCDEFGHIJK",
                    "thumbnail": "https://i.ytimg.com/vi/ABCDEFGHIJK/maxresdefault.jpg",
                }
            }

            SYNC.update_homepage(
                repo,
                23,
                {"headline": "Future episode", "date": "Future date", "desc": "Future summary."},
                videos,
            )

            html = (repo / "index.html").read_text()
            self.assertIn('class="latest-card" data-video-id="ABCDEFGHIJK"', html)
            self.assertNotIn('class="latest-card" data-video-id="f2yugYwXOBo"', html)
            self.assertNotIn('data-audio-src=', html)

    def test_homepage_sync_preserves_media_for_same_featured_episode(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "index.html").write_text(
                """
                <div class="latest-card" data-video-id="f2yugYwXOBo" data-audio-src="/audio/weekly-claw-22.mp3">
                  <div class="latest-number" aria-hidden="true">22</div>
                  <p class="latest-label">Featured latest episode · Previous date</p>
                  <h2 id="latest-title">Previous episode</h2>
                  <p class="latest-meta">Previous summary.</p>
                  <div class="latest-action"><a class="button" href="/episodes?week=22&amp;deck=main">Open episode <span>→</span></a></div>
                </div>
                """
            )

            SYNC.update_homepage(
                repo,
                22,
                {"headline": "Current episode", "date": "Current date", "desc": "Current summary."},
                {},
            )

            html = (repo / "index.html").read_text()
            self.assertIn('data-video-id="f2yugYwXOBo"', html)
            self.assertIn('data-audio-src="/audio/weekly-claw-22.mp3"', html)

    def test_homepage_sync_clears_stale_media_before_new_video_is_published(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "index.html").write_text(
                """
                <div class="latest-card" data-video-id="f2yugYwXOBo" data-audio-src="/audio/weekly-claw-22.mp3">
                  <div class="latest-number" aria-hidden="true">22</div>
                  <p class="latest-label">Featured latest episode · Previous date</p>
                  <h2 id="latest-title">Previous episode</h2>
                  <p class="latest-meta">Previous summary.</p>
                  <div class="latest-action"><a class="button" href="/episodes?week=22&amp;deck=main">Open episode <span>→</span></a></div>
                </div>
                """
            )

            SYNC.update_homepage(
                repo,
                23,
                {"headline": "Future episode", "date": "Future date", "desc": "Future summary."},
                {},
            )

            html = (repo / "index.html").read_text()
            self.assertIn('class="latest-card">', html)
            self.assertNotIn('data-video-id=', html)
            self.assertNotIn('data-audio-src=', html)

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
