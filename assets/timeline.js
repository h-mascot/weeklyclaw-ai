(() => {
  "use strict";

  const queryInput = document.getElementById("timeline-query");
  const searchForm = document.querySelector(".timeline-search");
  const status = document.querySelector("[data-search-status]");
  const list = document.querySelector("[data-timeline-list]");
  const orderButtons = [...document.querySelectorAll("[data-order]")];
  const entries = [...document.querySelectorAll(".timeline-entry")];
  let corpusPromise;
  let searchGeneration = 0;

  const themeToggle = document.querySelector("[data-theme-toggle]");
  const themeLabel = themeToggle?.querySelector("[data-theme-label]");
  const themeIcon = themeToggle?.querySelector("[data-theme-icon]");
  const setTheme = (theme) => {
    const dark = theme === "dark";
    document.documentElement.dataset.theme = dark ? "dark" : "light";
    themeToggle?.setAttribute("aria-pressed", String(dark));
    themeToggle?.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode");
    themeToggle?.setAttribute("title", dark ? "Switch to light mode" : "Switch to dark mode");
    if (themeLabel) themeLabel.textContent = dark ? "Light mode" : "Dark mode";
    if (themeIcon) themeIcon.textContent = dark ? "☀" : "☾";
    try { localStorage.setItem("weeklyclaw-theme", dark ? "dark" : "light"); } catch {}
  };
  setTheme(document.documentElement.dataset.theme || "light");
  themeToggle?.addEventListener("click", () => setTheme(document.documentElement.dataset.theme === "dark" ? "light" : "dark"));

  const normalize = (value) => String(value || "").trim().toLowerCase();
  const formatTimestamp = (seconds) => {
    if (typeof seconds !== "number" || !Number.isFinite(seconds) || seconds < 0) return "—";
    const whole = Math.floor(seconds);
    return `${Math.floor(whole / 60)}:${String(whole % 60).padStart(2, "0")}`;
  };

  const loadSearch = () => {
    corpusPromise ||= Promise.all([
      fetch("/public-episodes.json", { headers: { Accept: "application/json" } }).then((response) => {
        if (!response.ok) throw new Error(`Corpus request failed: ${response.status}`);
        return response.json();
      }),
      import("/assets/episode-search.mjs"),
    ]).then(([corpus, searchModule]) => {
      if (corpus?.schemaVersion !== 1 || !Array.isArray(corpus.episodes)) throw new Error("Unsupported public corpus");
      return searchModule.createEpisodeSearch(corpus);
    }).catch((error) => {
      corpusPromise = null;
      throw error;
    });
    return corpusPromise;
  };

  const clearHits = () => entries.forEach((entry) => {
    const results = entry.querySelector("[data-transcript-results]");
    const label = entry.querySelector("[data-hit-label]");
    results?.replaceChildren();
    if (results) results.hidden = true;
    if (label) label.hidden = true;
  });

  const renderPassages = (entry, group) => {
    const results = entry.querySelector("[data-transcript-results]");
    const label = entry.querySelector("[data-hit-label]");
    if (!results || !label) return;
    results.replaceChildren();
    (group?.passages || []).forEach((passage) => {
      const row = document.createElement("li");
      const link = document.createElement("a");
      const text = document.createElement("span");
      const isTranscript = passage.sourceType === "transcript" && passage.segmentId;
      link.className = "timestamp";
      link.textContent = isTranscript ? formatTimestamp(passage.startSeconds) : passage.sourceType === "summary" ? "Summary" : "Episode";
      link.href = isTranscript
        ? `/episodes/${encodeURIComponent(entry.dataset.week)}/#${encodeURIComponent(passage.segmentId)}`
        : `/episodes/${encodeURIComponent(entry.dataset.week)}/`;
      text.textContent = passage.snippet || "";
      row.append(link, text);
      results.append(row);
    });
    const hasResults = Boolean(group?.passages?.length);
    label.hidden = !hasResults;
    results.hidden = !hasResults;
  };

  const updateUrl = () => {
    const url = new URL(location.href);
    const query = queryInput?.value.trim() || "";
    const activeOrder = orderButtons.find((button) => button.getAttribute("aria-pressed") === "true")?.dataset.order;
    if (query) url.searchParams.set("q", query); else url.searchParams.delete("q");
    if (activeOrder === "oldest") url.searchParams.set("order", "oldest"); else url.searchParams.delete("order");
    history.replaceState(null, "", url);
  };

  async function applySearch() {
    const query = normalize(queryInput?.value);
    const generation = ++searchGeneration;
    if (!query) {
      clearHits();
      entries.forEach((entry) => {
        entry.querySelector(".timeline-summary").hidden = false;
        entry.hidden = false;
        entry.classList.remove("is-search-match");
      });
      if (status) status.textContent = `${entries.length} episodes`;
      return;
    }
    if (status) status.textContent = "Searching published summaries and transcript segments…";
    try {
      const search = await loadSearch();
      if (generation !== searchGeneration) return;
      const groups = new Map(search.searchGroups(query, { passagesPerEpisode: 3 }).map((group) => [String(group.episode.week), group]));
      let visible = 0;
      entries.forEach((entry) => {
        const group = groups.get(entry.dataset.week);
        const summaryMatch = Boolean(group?.passages?.some((passage) => passage.sourceType === "summary") || group?.titleMatch);
        renderPassages(entry, group);
        const hasMatch = Boolean(group);
        entry.querySelector(".timeline-summary").hidden = true;
        entry.hidden = !hasMatch;
        entry.classList.toggle("is-search-match", hasMatch);
        if (hasMatch) visible += 1;
      });
      if (status) status.textContent = `${visible} episodes match “${queryInput.value.trim()}”`;
    } catch {
      if (generation !== searchGeneration) return;
      clearHits();
      entries.forEach((entry) => {
        entry.querySelector(".timeline-summary").hidden = false;
        entry.hidden = false;
        entry.classList.remove("is-search-match");
      });
      if (status) status.textContent = "Transcript search is temporarily unavailable; summary archive restored.";
    }
  }

  function applyOrder(order, { updateHistory = true } = {}) {
    const ordered = [...entries].sort((a, b) => Number(a.dataset.week) - Number(b.dataset.week));
    if (order === "newest") ordered.reverse();
    ordered.forEach((entry) => list.append(entry));
    orderButtons.forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.order === order)));
    if (updateHistory) updateUrl();
  }

  const syncFromUrl = () => {
    const params = new URLSearchParams(location.search);
    if (queryInput) queryInput.value = params.get("q") || "";
    applyOrder(params.get("order") === "oldest" ? "oldest" : "newest", { updateHistory: false });
    applySearch();
  };

  queryInput?.addEventListener("input", () => { updateUrl(); applySearch(); });
  searchForm?.addEventListener("submit", (event) => {
    event.preventDefault();
    updateUrl();
    applySearch();
  });
  orderButtons.forEach((button) => button.addEventListener("click", () => applyOrder(button.dataset.order)));
  window.addEventListener("popstate", syncFromUrl);
  syncFromUrl();
})();
