const previews = {
  inference: {
    kicker: "Live product",
    title: "Inference Brief",
    summary: "A working AI-news reader built for people who want the signal without living in feeds.",
    image: "./assets/inference-brief.png",
    imageAlt: "Inference Brief issue and article interface",
    role: "Product + data pipeline",
    status: "Live",
    focus: "AI news workflow",
    problem:
      "AI news is noisy, repetitive, and easy to over-skim. Inference Brief turns source collection, scoring, summarisation, issue publishing, and reader history into one product flow.",
    points: [
      "Collects and scores stories before they become reader-facing issues.",
      "Packages summaries, bookmarks, account history, and preferences around the reading job.",
      "Built as a real product rather than a static newsletter archive."
    ],
    stack: ["Next.js", "TypeScript", "Supabase", "Python", "Stripe"],
    links: [
      { label: "Open product", href: "https://inferencebrief.co/", primary: true },
      { label: "Read case study", href: "https://github.com/MatthewPaver/MatthewPaver/blob/main/CASE_STUDIES.md#inference-brief" }
    ],
    note: "Motion is deliberately kept out of the first store view. The still shows the actual product state faster."
  },
  happening: {
    kicker: "Private system",
    title: "Happening",
    summary: "A venue-event ingestion system that turns inconsistent public pages into checked event data.",
    image: "./assets/happening-web.png",
    imageAlt: "Happening event feed, source drawer, and map interface",
    role: "Crawler + reliability system",
    status: "Private",
    focus: "103+ venue sources",
    problem:
      "Venue listings are scattered across pages with different layouts, calendars, markup, and failure modes. Happening treats each source as a configured data contract with extraction, dedupe, validation, and regression tests.",
    points: [
      "Uses source configs so behaviour is explicit and reviewable.",
      "Combines crawling, extraction, dedupe, checks, and scheduled runs.",
      "Backed by a 167-test private reliability suite across the ingestion surface."
    ],
    stack: ["Python", "Playwright", "SQLite", "Pydantic", "GitHub Actions"],
    links: [
      { label: "Read case study", href: "https://github.com/MatthewPaver/MatthewPaver/blob/main/CASE_STUDIES.md#featured-build-happening", primary: true }
    ],
    note: "The preview uses a real interface screenshot rather than a pipeline diagram, so the system reads as a usable product."
  },
  quicksupply: {
    kicker: "Workflow app",
    title: "QuickSupply",
    summary: "A supply-cover workflow for requests, agencies, teacher offers, compliance, and live status.",
    image: "./assets/quicksupply-dashboard.png",
    imageAlt: "QuickSupply agency dashboard interface",
    role: "Workflow product",
    status: "Private MVP",
    focus: "School cover ops",
    problem:
      "School cover coordination can become a spreadsheet-and-message chain. QuickSupply shapes the job around request intake, sequential agency assignment, teacher availability, compliance checks, and status updates.",
    points: [
      "Separates school, agency, and teacher workflows instead of flattening them into one admin view.",
      "Uses live status updates so bookings can move without manual chasing.",
      "Designed around operational clarity: who has the request, what changed, and what happens next."
    ],
    stack: ["Next.js", "TypeScript", "PostgreSQL", "Drizzle", "SSE"],
    links: [
      { label: "View catalogue card", href: "./#quicksupply", primary: true }
    ],
    note: "A still preview is more effective here than a fast GIF because the value is the workflow structure, not animation."
  }
};

function setText(id, text) {
  const node = document.querySelector(`#${id}`);
  if (node) node.textContent = text;
}

function renderPreview() {
  const params = new URLSearchParams(window.location.search);
  const slug = params.get("app") || "inference";
  const preview = previews[slug] || previews.inference;

  document.title = `${preview.title} · Matthew Paver Portfolio Store`;
  setText("preview-kicker", preview.kicker);
  setText("preview-title", preview.title);
  setText("preview-summary", preview.summary);
  setText("preview-role", preview.role);
  setText("preview-status", preview.status);
  setText("preview-focus", preview.focus);
  setText("preview-problem", preview.problem);
  setText("preview-note", preview.note);

  const image = document.querySelector("#preview-image");
  if (image) {
    image.src = preview.image;
    image.alt = preview.imageAlt;
  }

  const actions = document.querySelector("#preview-actions");
  if (actions) {
    actions.replaceChildren(
      ...preview.links.map((link) => {
        const anchor = document.createElement("a");
        anchor.className = `button ${link.primary ? "primary" : "ghost"}`;
        anchor.href = link.href;
        anchor.textContent = link.label;
        return anchor;
      })
    );
  }

  const points = document.querySelector("#preview-points");
  if (points) {
    points.replaceChildren(
      ...preview.points.map((point) => {
        const item = document.createElement("li");
        item.textContent = point;
        return item;
      })
    );
  }

  const stack = document.querySelector("#preview-stack");
  if (stack) {
    stack.replaceChildren(
      ...preview.stack.map((item) => {
        const badge = document.createElement("span");
        badge.textContent = item;
        return badge;
      })
    );
  }
}

document.addEventListener("DOMContentLoaded", renderPreview);
