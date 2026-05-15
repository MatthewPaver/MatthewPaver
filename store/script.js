const filters = Array.from(document.querySelectorAll(".filter"));
const cards = Array.from(document.querySelectorAll(".app-card"));

function setFilter(filterName) {
  filters.forEach((button) => {
    button.classList.toggle("active", button.dataset.filter === filterName);
  });

  cards.forEach((card) => {
    const tags = card.dataset.tags.split(" ");
    const isVisible = filterName === "all" || tags.includes(filterName);
    card.classList.toggle("hidden", !isVisible);
  });
}

filters.forEach((button) => {
  button.addEventListener("click", () => {
    setFilter(button.dataset.filter);
  });
});
