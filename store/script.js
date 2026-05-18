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

  const searchIndex = new Map();

  function initCardDetails() {
    cards.forEach((card, index) => {
      const title = card.querySelector("h3")?.textContent?.trim();
      const titleRow = card.querySelector(".app-title-row");
      const proofList = card.querySelector(".proof-list");
      const solves = card.dataset.solves;
      const shows = card.dataset.shows;

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

      if (solves && shows && proofList && !card.querySelector(".card-snapshot")) {
        const snapshot = document.createElement("dl");
        snapshot.className = "card-snapshot";
        snapshot.innerHTML = `
          <div>
            <dt>Solves</dt>
            <dd></dd>
          </div>
          <div>
            <dt>Shows</dt>
            <dd></dd>
          </div>
        `;
        snapshot.querySelectorAll("dd")[0].textContent = solves;
        snapshot.querySelectorAll("dd")[1].textContent = shows;
        proofList.insertAdjacentElement("afterend", snapshot);
      }

      searchIndex.set(card, card.textContent.toLowerCase());
    });
  }

  function initRevealMotion() {
    const targets = Array.from(
      document.querySelectorAll(".selected-card, .credential-group a, .featured-build, .personal-note, .shelf-grid a, .app-card")
    );

    if (prefersReducedMotion) return;

    targets.forEach((target, index) => {
      target.classList.add("reveal-item");
      target.style.setProperty("--reveal-index", String(index % 6));
    });

    const reveal = (target) => target.classList.add("is-visible");

    // Reveal anything already in the initial viewport synchronously so nothing
    // sits at opacity:0 on first paint (e.g. headless captures, fast scrolls).
    targets.forEach((target) => {
      const rect = target.getBoundingClientRect();
      if (rect.top < window.innerHeight + 120) reveal(target);
    });

    if (!("IntersectionObserver" in window)) {
      targets.forEach(reveal);
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          reveal(entry.target);
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -2% 0px", threshold: 0.05 }
    );

    targets.forEach((target) => {
      if (!target.classList.contains("is-visible")) observer.observe(target);
    });

    // Safety net: anything still hidden after 1.5s is forced visible. Catches
    // headless renderers, broken IO implementations, and pages that never get
    // scrolled into view (search engines, social-card crawlers).
    window.setTimeout(() => targets.forEach(reveal), 1500);
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

  initRevealMotion();
  initScrollChrome();
  initSpotlightCards();
  initCountUp();
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

function initCountUp() {
  const targets = document.querySelectorAll("[data-count-to]");
  if (!targets.length) return;

  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    targets.forEach((node) => {
      node.textContent = node.dataset.countTo;
    });
    return;
  }

  const animate = (node) => {
    const target = Number(node.dataset.countTo) || 0;
    const duration = 900 + Math.min(900, target * 6);
    const start = performance.now();
    node.textContent = "0";
    const step = (now) => {
      const progress = Math.min(1, (now - start) / duration);
      const eased = 1 - Math.pow(1 - progress, 3);
      node.textContent = String(Math.round(target * eased));
      if (progress < 1) window.requestAnimationFrame(step);
      else node.textContent = String(target);
    };
    window.requestAnimationFrame(step);
  };

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        animate(entry.target);
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.4 }
  );

  targets.forEach((node) => observer.observe(node));
}
