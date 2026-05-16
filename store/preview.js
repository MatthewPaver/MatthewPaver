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
  },
  study: {
    kicker: "Private product",
    title: "AI Study Companion",
    summary: "A study workflow for turning uploaded notes into flashcards, quizzes, plans, and review sessions.",
    image: "./assets/ai-study-companion.png",
    imageAlt: "AI Study Companion product workspace",
    role: "AI learning workflow",
    status: "Private",
    focus: "Study material generation",
    problem:
      "Revision material often starts as a pile of documents and notes. This product shape turns those inputs into structured practice: cards, quizzes, plans, and spaced review.",
    points: [
      "Ingests PDF, DOCX, and text material before generating study assets.",
      "Separates background generation jobs from the learner-facing review flow.",
      "Uses a spaced-repetition loop so the product is about retention, not just content generation."
    ],
    stack: ["FastAPI", "PostgreSQL", "Redis", "Celery", "LLMs"],
    links: [
      { label: "Read case study", href: "https://github.com/MatthewPaver/MatthewPaver/blob/main/CASE_STUDIES.md#ai-study-companion", primary: true }
    ],
    note: "This is a private build, so the preview focuses on the workflow and system decisions rather than exposing code."
  },
  "smart-job": {
    kicker: "Private system",
    title: "Smart Job Market Intelligence",
    summary: "A labour-market signal layer for turning listings into salary, skill, remote-work, and volume trends.",
    image: "./assets/smart-job-market.png",
    imageAlt: "Smart Job Market Intelligence interface",
    role: "Data product",
    status: "Private",
    focus: "Job-market signals",
    problem:
      "Job listings are noisy snapshots. This system normalises listings and turns them into repeatable reports and alerts that are easier to compare over time.",
    points: [
      "Normalises listing data so trend analysis has a consistent base.",
      "Packages salary, skill, volume, and remote-work signals into usable outputs.",
      "Frames the product around alerts, reports, and API tiers rather than one-off analysis."
    ],
    stack: ["Python", "FastAPI", "PostgreSQL", "Redis", "Celery"],
    links: [
      { label: "Read case study", href: "https://github.com/MatthewPaver/MatthewPaver/blob/main/CASE_STUDIES.md#smart-job-market-intelligence", primary: true }
    ],
    note: "The preview keeps the emphasis on the decision-support workflow: collect, normalise, compare, alert."
  },
  operations: {
    kicker: "Private prototype",
    title: "Operations Platform Prototype",
    summary: "A property-operations concept for resident requests, audit trails, payments, and AI-assisted triage.",
    image: "./assets/operations-platform.png",
    imageAlt: "Operations platform prototype interface",
    role: "Workflow prototype",
    status: "Private",
    focus: "Operations triage",
    problem:
      "Operational requests get messy when status, ownership, evidence, payment context, and triage notes live in different places. This prototype brings that work into one interface model.",
    points: [
      "Models resident request intake and operations follow-up as a traceable workflow.",
      "Includes audit trail and service-charge visibility concepts.",
      "Explores where AI triage can help without hiding operational accountability."
    ],
    stack: ["Next.js", "TypeScript", "Payments", "AI triage", "Product docs"],
    links: [
      { label: "View catalogue", href: "./#store", primary: true }
    ],
    note: "This sits in the store as a product prototype: useful for showing product thinking, not as a public repo."
  },
  lakehouse: {
    kicker: "Public application",
    title: "Marketing ML Lakehouse",
    summary: "A local analytics loop that moves raw marketing CSVs through DuckDB, model training, checks, and a dashboard.",
    image: "./assets/marketing-lakehouse.svg",
    imageAlt: "Marketing ML Lakehouse workflow visual",
    role: "Analytics engineering",
    status: "Public",
    focus: "Lakehouse + ML",
    problem:
      "Many analytics demos stop at a notebook. This repo packages the full local loop: ingest raw marketing data, model it, check it, and expose it through a dashboard.",
    points: [
      "Uses a bronze, silver, and gold flow to make the data path inspectable.",
      "Includes model training and data-quality checks rather than only charts.",
      "Has repo packaging and validation so reviewers can inspect it as a runnable project."
    ],
    stack: ["Python", "DuckDB", "XGBoost", "Streamlit", "Makefile"],
    links: [
      { label: "Open repo", href: "https://github.com/MatthewPaver/marketing-ml-lakehouse", primary: true }
    ],
    note: "This is one of the better public repos to inspect because it shows an end-to-end data application shape."
  },
  projectlens: {
    kicker: "Public application",
    title: "ProjectLens",
    summary: "A schedule-risk app for turning project updates into slippage, milestone, and forecast outputs.",
    image: "./assets/projectlens-thumb.svg",
    imageAlt: "ProjectLens schedule risk product thumbnail",
    role: "Analytics product",
    status: "Public",
    focus: "Delivery risk",
    problem:
      "Schedule data can be hard to read until the risk is already obvious. ProjectLens packages upload, cleaning, slippage analysis, milestone pressure, and reporting into a clearer workflow.",
    points: [
      "Turns project schedule inputs into risk and slippage outputs.",
      "Packages analysis into reporting views rather than leaving it as raw tables.",
      "Includes tests and validation so the public repo is more reviewer-friendly."
    ],
    stack: ["Python", "Flask", "pandas", "Forecasting", "Power BI"],
    links: [
      { label: "Open repo", href: "https://github.com/MatthewPaver/ProjectLens", primary: true }
    ],
    note: "The preview thumbnail is standardised so the store reads as a product shelf, while the repo still contains the detailed dashboard material."
  },
  architexa: {
    kicker: "Public ML project",
    title: "Architexa",
    summary: "A compact architecture image-generation project built around dataset prep, conditional GAN training, and a small API.",
    image: "./assets/architexa-preview.svg",
    imageAlt: "Architexa architecture image generation workflow",
    role: "Generative ML",
    status: "Public",
    focus: "Architecture imagery",
    problem:
      "The project explores image generation for architecture-style outputs, including how the data is prepared, how the model is trained, and how generated outputs can be served.",
    points: [
      "Curates image data before model training.",
      "Uses a conditional GAN workflow for generation.",
      "Exposes model interaction through a small Flask API."
    ],
    stack: ["Python", "TensorFlow", "Keras", "Flask", "GAN"],
    links: [
      { label: "Open repo", href: "https://github.com/MatthewPaver/Architexa", primary: true }
    ],
    note: "This is best treated as an ML experiment: useful for showing model-building range, not a flagship product."
  },
  recommender: {
    kicker: "Public ML project",
    title: "Dating App Recommendation System",
    summary: "A recommendation project focused on implicit-feedback ranking, temporal holdouts, and Top-K metrics.",
    image: "./assets/recommender-metrics.svg",
    imageAlt: "Dating app recommendation metrics visual",
    role: "Ranking system",
    status: "Public",
    focus: "Recommendation evaluation",
    problem:
      "Recommendation demos often skip the evaluation question. This project uses swipe-style interaction data and temporal splitting to make ranking performance easier to reason about.",
    points: [
      "Builds candidate ranking from implicit interaction data.",
      "Uses temporal holdouts so evaluation is closer to real recommendation timing.",
      "Includes sample data, tests, and a CLI smoke path for public review."
    ],
    stack: ["Python", "NumPy", "SciPy", "Jupyter", "CLI"],
    links: [
      { label: "Open repo", href: "https://github.com/MatthewPaver/dating-app-recommendation-system", primary: true }
    ],
    note: "This preview is about evaluation discipline: how the recommender is tested matters as much as the model choice."
  },
  hr: {
    kicker: "Public dashboard package",
    title: "HR Performance Analytics",
    summary: "A Power BI dashboard package for headcount, sales performance, absence, and stakeholder-ready reporting.",
    image: "./assets/hr-performance-thumb.svg",
    imageAlt: "HR Performance Analytics product thumbnail",
    role: "BI reporting",
    status: "Public",
    focus: "People analytics",
    problem:
      "Dashboard work is only useful when someone can understand the business question and inspect the handoff material. This package keeps screenshots, PBIX files, data, and commentary together.",
    points: [
      "Covers summary, sales, and absence views.",
      "Includes prepared data and dashboard files for inspection.",
      "Frames the work as a handoff package rather than a single screenshot."
    ],
    stack: ["Power BI", "DAX", "CSV", "Reporting", "PDF exports"],
    links: [
      { label: "Open repo", href: "https://github.com/MatthewPaver/hr-performance-dashboards", primary: true }
    ],
    note: "The store uses a standardised thumbnail; the repo remains the place for the full dashboard evidence."
  },
  sentence: {
    kicker: "Public NLP demo",
    title: "Sentence Similarity Analysis",
    summary: "A compact NLP notebook showing embeddings, cosine ranking, and the limits of similarity as a signal.",
    image: "./assets/sentence-similarity.svg",
    imageAlt: "Sentence similarity embedding workflow",
    role: "NLP analysis",
    status: "Public",
    focus: "Embedding retrieval",
    problem:
      "Similarity search is useful, but similarity is not the same as truth. This notebook is a small, focused demo of embedding comparison and retrieval caveats.",
    points: [
      "Uses transformer embeddings to compare sentence meaning.",
      "Ranks examples with cosine similarity.",
      "Calls out where retrieval-style scoring can mislead."
    ],
    stack: ["Python", "Jupyter", "sentence-transformers", "PyTorch"],
    links: [
      { label: "Open repo", href: "https://github.com/MatthewPaver/sentence-similarity-analysis", primary: true }
    ],
    note: "This is intentionally small: it works as a clear NLP concept demo in the broader portfolio."
  },
  archive: {
    kicker: "Archive shelf",
    title: "Newsletter + Scraper Utilities",
    summary: "Earlier automation utilities kept for provenance: newsletter rendering and image collection patterns.",
    image: "./assets/archive-utilities-thumb.svg",
    imageAlt: "Newsletter and scraper utilities archive visual",
    role: "Earlier automation",
    status: "Archived",
    focus: "Superseded utilities",
    problem:
      "Not every project should be presented as current flagship work. These utilities show earlier automation patterns that fed later product and data experiments.",
    points: [
      "Article-to-HTML newsletter rendering helped shape later publishing workflows.",
      "Image collection utilities supported earlier dataset experiments.",
      "Kept in the store as archive context, not as the first thing to inspect."
    ],
    stack: ["Python", "HTML", "Automation", "Scraping"],
    links: [
      { label: "Newsletter repo", href: "https://github.com/MatthewPaver/generate-newsletter", primary: true },
      { label: "Scraper repo", href: "https://github.com/MatthewPaver/pinterest-image-scraper" }
    ],
    note: "This preview is deliberately honest: archived work can be useful evidence without competing with the strongest builds."
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
