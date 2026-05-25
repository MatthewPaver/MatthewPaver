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
  const searchIndex = new Map();

  function initCardDetails() {
    cards.forEach((card, index) => {
      const title = card.querySelector("h3")?.textContent?.trim();
      const titleRow = card.querySelector(".app-title-row");
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

      searchIndex.set(card, card.textContent.toLowerCase());
    });
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
      const matchesSearch = !query || (searchIndex.get(card) || "").includes(query);
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

    if (announcer) {
      announcer.textContent =
        count === 0
          ? "Nothing matches that filter combination. Clear the search or choose All to see every project."
          : `${count} projects showing`;
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

  initScrollChrome();
  initSpotlightCards();
});

function initScrollChrome() {
  const progress = document.querySelector(".scroll-progress");
  const topbar = document.querySelector(".topbar-shell");
  if (!progress && !topbar) return;

  let ticking = false;
  const update = () => {
    const scrolled = window.scrollY;
    const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    if (progress) progress.style.width = `${Math.min(100, (scrolled / max) * 100)}%`;
    if (topbar) topbar.classList.toggle("is-scrolled", scrolled > 12);
    ticking = false;
  };
  window.addEventListener(
    "scroll",
    () => {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    },
    { passive: true }
  );
  update();
}

function initSpotlightCards() {
  const cards = document.querySelectorAll(".selected-card, .app-card.featured");
  if (!cards.length) return;
  const fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  if (!fine) return;

  cards.forEach((card) => {
    card.addEventListener("mousemove", (event) => {
      const rect = card.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width) * 100;
      const y = ((event.clientY - rect.top) / rect.height) * 100;
      card.style.setProperty("--mx", `${x}%`);
      card.style.setProperty("--my", `${y}%`);
    });
  });
}
