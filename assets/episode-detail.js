(() => {
  "use strict";

  const tabs = [...document.querySelectorAll('[role="tab"]')];
  const panels = tabs.map((tab) => document.getElementById(tab.getAttribute("aria-controls"))).filter(Boolean);
  document.documentElement.classList.add("js-ready");
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
  const activate = (tab, moveFocus = true) => {
    tabs.forEach((candidate) => {
      const selected = candidate === tab;
      candidate.setAttribute("aria-selected", String(selected));
      candidate.tabIndex = selected ? 0 : -1;
    });
    panels.forEach((panel) => { panel.hidden = panel.getAttribute("aria-labelledby") !== tab.id; });
    if (moveFocus) tab.focus();
  };
  tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => activate(tab, false));
    tab.addEventListener("keydown", (event) => {
      if (!["ArrowRight", "ArrowLeft", "Home", "End"].includes(event.key)) return;
      event.preventDefault();
      const nextIndex = event.key === "Home" ? 0 : event.key === "End" ? tabs.length - 1 : (index + (event.key === "ArrowRight" ? 1 : -1) + tabs.length) % tabs.length;
      activate(tabs[nextIndex]);
    });
  });
  const initiallySelected = tabs.find((tab) => tab.getAttribute("aria-selected") === "true") || tabs[0];
  if (initiallySelected) activate(initiallySelected, false);

  const search = document.querySelector("[data-transcript-search]");
  const status = document.querySelector("[data-transcript-status]");
  const rows = [...document.querySelectorAll("[data-transcript-text]")];
  const transcriptGroups = [...document.querySelectorAll("[data-speaker-group]")];
  const applyTranscriptSearch = () => {
    const query = search?.value.trim().toLowerCase() || "";
    const visibleGroups = new Map();
    let visible = 0;
    rows.forEach((row) => {
      const matches = !query || row.dataset.transcriptText.includes(query);
      row.hidden = !matches;
      if (!matches) return;
      visible += 1;
      const group = row.closest("[data-speaker-group]");
      if (group) visibleGroups.set(group, (visibleGroups.get(group) || 0) + 1);
    });
    transcriptGroups.forEach((group) => { group.hidden = Boolean(query) && !visibleGroups.has(group); });
    if (status) status.textContent = query ? `${visible} matching published segments` : `${rows.length} published segments`;
  };
  search?.addEventListener("input", applyTranscriptSearch);

  const video = document.querySelector(".video-frame iframe");
  const seekVideo = (seconds) => {
    if (!video || !Number.isFinite(seconds)) return;
    try {
      const url = new URL(video.src);
      url.searchParams.set("start", String(Math.floor(seconds)));
      video.src = url.href;
    } catch {}
  };
  document.querySelectorAll("[data-start-seconds]").forEach((link) => link.addEventListener("click", () => seekVideo(Number(link.dataset.startSeconds))));
  const activateHashTarget = () => {
    if (!location.hash) return;
    let id = location.hash.slice(1);
    try { id = decodeURIComponent(id); } catch {}
    const target = document.getElementById(id);
    if (target && target.matches("[data-transcript-text]")) {
      const transcriptTab = document.getElementById("transcript-tab");
      if (transcriptTab) activate(transcriptTab, false);
      const timestamp = target.querySelector("[data-start-seconds]")?.dataset.startSeconds;
      seekVideo(Number(timestamp));
      window.requestAnimationFrame(() => target.scrollIntoView({ block: "start" }));
    }
  };
  window.addEventListener("hashchange", activateHashTarget);
  activateHashTarget();
})();
