document.addEventListener("DOMContentLoaded", () => {
  const filters = Array.from(document.querySelectorAll(".filter"));
  const cards = Array.from(document.querySelectorAll(".app-card"));
  const searchInput = document.querySelector("#store-search");
  const sortSelect = document.querySelector("#store-sort");
  const clearSearch = document.querySelector("#clear-search");
  const visibleCount = document.querySelector("#visible-count");
  const emptyState = document.querySelector(".empty-state");
  const storeGrid = document.querySelector(".store-grid");
  const archiveShelf = document.querySelector(".archive-shelf");
  const announcer = document.querySelector("#store-filter-announcement");

  if (!searchInput || !visibleCount || !emptyState) return;

  let activeFilter = "all";
  const validFilters = new Set(filters.map((button) => button.dataset.filter).filter(Boolean));
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const cardSpecs = {
    "Inference Brief": ["Cuts through AI-news noise", "Live product workflow"],
    "Happening": ["Turns venue pages into data", "103+ sources, 167 tests"],
    "AI Study Companion": ["Makes revision material usable", "Ingestion + generation loop"],
    "Smart Job Market Intelligence": ["Finds labour-market signals", "Reports, alerts, API shape"],
    "QuickSupply": ["Coordinates supply-cover work", "Three-sided workflow model"],
    "Operations Platform Prototype": ["Organises property ops requests", "Audit trail + triage concept"],
    "Marketing ML Lakehouse": ["Packages local analytics", "Pipeline, ML, dashboard"],
    "ProjectLens": ["Reads schedule delivery risk", "Upload-to-report flow"],
    "Architexa": ["Generates architecture imagery", "Dataset, GAN, API"],
    "Dating App Recommendation System": ["Ranks candidate profiles", "Temporal evaluation discipline"],
    "HR Performance Analytics": ["Turns HR data into decisions", "Stakeholder-ready dashboards"],
    "Sentence Similarity Analysis": ["Compares meaning with embeddings", "Retrieval caveats made clear"],
    "Newsletter + Scraper Utilities": ["Archives earlier automation", "Useful provenance, not front door"]
  };

  function initCardDetails() {
    cards.forEach((card, index) => {
      const title = card.querySelector("h3")?.textContent?.trim();
      const spec = title ? cardSpecs[title] : null;
      const titleRow = card.querySelector(".app-title-row");
      const proofList = card.querySelector(".proof-list");

      card.style.setProperty("--card-number", `"${String(index + 1).padStart(2, "0")}"`);
      card.dataset.order = String(index);
      if (title) card.dataset.title = title;

      if (titleRow && title && !titleRow.querySelector(".app-icon")) {
        const icon = document.createElement("span");
        icon.className = "app-icon";
        icon.setAttribute("aria-hidden", "true");
        icon.textContent = title
          .split(/\s+/)
          .filter(Boolean)
          .slice(0, 2)
          .map((word) => word[0])
          .join("")
          .toUpperCase();
        titleRow.prepend(icon);
      }

      if (!spec || !proofList || card.querySelector(".card-snapshot")) return;

      const snapshot = document.createElement("dl");
      snapshot.className = "card-snapshot";
      snapshot.innerHTML = `
        <div>
          <dt>Solves</dt>
          <dd>${spec[0]}</dd>
        </div>
        <div>
          <dt>Shows</dt>
          <dd>${spec[1]}</dd>
        </div>
      `;
      proofList.insertAdjacentElement("afterend", snapshot);
    });
  }

  function initRevealMotion() {
    if (prefersReducedMotion || !("IntersectionObserver" in window)) return;

    const targets = Array.from(
      document.querySelectorAll(".selected-card, .credential-group a, .featured-build, .personal-note, .shelf-grid a, .app-card")
    );

    targets.forEach((target, index) => {
      target.classList.add("reveal-item");
      target.style.setProperty("--reveal-index", String(index % 6));
    });

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -10% 0px", threshold: 0.12 }
    );

    targets.forEach((target) => observer.observe(target));
  }

  function updateUrlState() {
    const url = new URL(window.location.href);
    const query = searchInput.value.trim();
    const sortMode = sortSelect?.value || "curated";

    if (activeFilter === "all") {
      url.searchParams.delete("filter");
    } else {
      url.searchParams.set("filter", activeFilter);
    }

    if (query) {
      url.searchParams.set("q", query);
    } else {
      url.searchParams.delete("q");
    }

    if (sortMode === "curated") {
      url.searchParams.delete("sort");
    } else {
      url.searchParams.set("sort", sortMode);
    }

    window.history.replaceState({}, "", url);
  }

  function sortCards() {
    if (!storeGrid || !sortSelect) return;

    const sortedCards = [...cards].sort((a, b) => {
      if (sortSelect.value === "alpha") {
        return (a.dataset.title || "").localeCompare(b.dataset.title || "");
      }

      if (sortSelect.value === "public") {
        const aPublic = a.dataset.status?.toLowerCase().includes("public") || a.querySelector(".status.public");
        const bPublic = b.dataset.status?.toLowerCase().includes("public") || b.querySelector(".status.public");
        if (Boolean(aPublic) !== Boolean(bPublic)) return aPublic ? -1 : 1;
      }

      return Number(a.dataset.order || 0) - Number(b.dataset.order || 0);
    });

    sortedCards.forEach((card) => storeGrid.append(card));
  }

  function updateStore({ syncUrl = true } = {}) {
    const query = searchInput.value.trim().toLowerCase();
    let count = 0;

    sortCards();

    cards.forEach((card) => {
      const tags = (card.dataset.tags || "").split(" ");
      const matchesFilter = activeFilter === "all" || tags.includes(activeFilter);
      const matchesSearch = !query || card.textContent.toLowerCase().includes(query);
      const isVisible = matchesFilter && matchesSearch;
      card.classList.toggle("hidden", !isVisible);
      if (isVisible) count += 1;
    });

    if (archiveShelf) {
      const archiveCard = archiveShelf.querySelector(".app-card");
      archiveShelf.hidden = archiveCard?.classList.contains("hidden") ?? true;
    }

    visibleCount.textContent = String(count);
    emptyState.hidden = count > 0;
    if (clearSearch) clearSearch.hidden = searchInput.value.length === 0;
    if (syncUrl) updateUrlState();

    // Single polite live region so empty results get announced without duplicating the grid
    if (announcer) {
      announcer.textContent =
        count === 0
          ? "No ideas match your search or filters. Try clearing the search or choosing All."
          : `${count} ideas showing`;
    }
  }

  function setFilter(filterName) {
    activeFilter = filterName;
    filters.forEach((button) => {
      const isActive = button.dataset.filter === filterName;
      button.classList.toggle("active", isActive);
      button.setAttribute("aria-pressed", String(isActive));
    });

    updateStore();
  }

  filters.forEach((button) => {
    button.addEventListener("click", () => {
      setFilter(button.dataset.filter);
    });
  });

  document.querySelectorAll("[data-filter-link]").forEach((link) => {
    link.addEventListener("click", (event) => {
      const filterName = link.dataset.filterLink;
      if (!filterName || !validFilters.has(filterName)) return;
      event.preventDefault();
      setFilter(filterName);
      const target = document.querySelector("#project-grid-heading");
      if (target) {
        window.requestAnimationFrame(() => target.scrollIntoView({ block: "start" }));
      }
    });
  });

  searchInput.addEventListener("input", updateStore);
  sortSelect?.addEventListener("change", updateStore);
  if (clearSearch) {
    clearSearch.addEventListener("click", () => {
      searchInput.value = "";
      updateStore();
      searchInput.focus();
    });
  }

  const initialParams = new URLSearchParams(window.location.search);
  const initialFilter = initialParams.get("filter");
  const initialQuery = initialParams.get("q");
  const initialSort = initialParams.get("sort");

  initCardDetails();

  if (initialQuery) {
    searchInput.value = initialQuery;
  }

  if (sortSelect && ["curated", "public", "alpha"].includes(initialSort)) {
    sortSelect.value = initialSort;
  }

  if (initialFilter && validFilters.has(initialFilter)) {
    setFilter(initialFilter);
  } else {
    updateStore({ syncUrl: false });
  }

  initRevealMotion();
});
