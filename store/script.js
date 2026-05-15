document.addEventListener("DOMContentLoaded", () => {
  const filters = Array.from(document.querySelectorAll(".filter"));
  const cards = Array.from(document.querySelectorAll(".app-card"));
  const searchInput = document.querySelector("#store-search");
  const clearSearch = document.querySelector("#clear-search");
  const visibleCount = document.querySelector("#visible-count");
  const emptyState = document.querySelector(".empty-state");
  const announcer = document.querySelector("#store-filter-announcement");
  const collectionLinks = Array.from(document.querySelectorAll("[data-collection]"));

  if (!searchInput || !visibleCount || !emptyState) return;

  let activeFilter = "all";

  function updateStore() {
    const query = searchInput.value.trim().toLowerCase();
    let count = 0;

    cards.forEach((card) => {
      const tags = (card.dataset.tags || "").split(" ");
      const matchesFilter = activeFilter === "all" || tags.includes(activeFilter);
      const matchesSearch = !query || card.textContent.toLowerCase().includes(query);
      const isVisible = matchesFilter && matchesSearch;
      card.classList.toggle("hidden", !isVisible);
      if (isVisible) count += 1;
    });

    visibleCount.textContent = String(count);
    emptyState.hidden = count > 0;
    if (clearSearch) clearSearch.hidden = searchInput.value.length === 0;

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

  collectionLinks.forEach((link) => {
    link.addEventListener("click", () => {
      setFilter(link.dataset.collection);
    });
  });

  searchInput.addEventListener("input", updateStore);
  if (clearSearch) {
    clearSearch.addEventListener("click", () => {
      searchInput.value = "";
      updateStore();
      searchInput.focus();
    });
  }

  updateStore();
});
