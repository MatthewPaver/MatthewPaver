import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const requiredColumns = ["slug", "title", "shelf", "status", "kind", "problem", "proof", "stack", "preview", "asset"];
const allowedShelves = new Set(["product", "data", "automation", "ml", "analytics", "archive"]);
const specDirectory = "specs/001-portfolio-store-reliability";
const requiredSpecFiles = [
  ".specify/memory/constitution.md",
  `${specDirectory}/spec.md`,
  `${specDirectory}/plan.md`,
  `${specDirectory}/research.md`,
  `${specDirectory}/quickstart.md`,
  `${specDirectory}/tasks.md`,
  `${specDirectory}/contracts/store-catalogue.md`
];

function readFile(relativePath) {
  return fs.readFileSync(path.join(root, relativePath), "utf8");
}

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = "";
  let inQuotes = false;

  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    const next = text[i + 1];

    if (char === '"' && inQuotes && next === '"') {
      field += '"';
      i += 1;
    } else if (char === '"') {
      inQuotes = !inQuotes;
    } else if (char === "," && !inQuotes) {
      row.push(field);
      field = "";
    } else if ((char === "\n" || char === "\r") && !inQuotes) {
      if (char === "\r" && next === "\n") i += 1;
      row.push(field);
      if (row.some((value) => value.trim())) rows.push(row);
      row = [];
      field = "";
    } else {
      field += char;
    }
  }

  if (field || row.length) {
    row.push(field);
    if (row.some((value) => value.trim())) rows.push(row);
  }

  const [headers, ...records] = rows;
  return records.map((record) =>
    Object.fromEntries(headers.map((header, index) => [header.trim(), (record[index] || "").trim()]))
  );
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

const indexRows = parseCsv(readFile("store/app-index.csv"));
const tagRows = parseCsv(readFile("store/tags.csv"));
const catalogueRows = parseCsv(readFile("store/catalogue.csv"));
const indexHtml = readFile("store/index.html");
const previewHtml = readFile("store/preview.html");
const previewJs = readFile("store/preview.js");
const storeScript = readFile("store/script.js");
const storeCss = readFile("store/styles.css");

const slugs = new Set();
const tagSet = new Set(tagRows.map((row) => row.tag));

assert(indexRows.length >= 10, "store/app-index.csv should include the full project catalogue");
assert(tagRows.length >= 6, "store/tags.csv should include the store shelves");

for (const row of indexRows) {
  for (const column of requiredColumns) {
    assert(row[column], `Missing ${column} for ${row.slug || row.title || "unknown row"}`);
  }

  assert(!slugs.has(row.slug), `Duplicate slug in app index: ${row.slug}`);
  slugs.add(row.slug);
  assert(allowedShelves.has(row.shelf), `Unknown shelf "${row.shelf}" for ${row.slug}`);
  assert(tagSet.has(row.shelf), `Shelf "${row.shelf}" is missing from tags.csv`);
  assert(row.preview === `preview.html?app=${row.slug}`, `Preview link should match slug for ${row.slug}`);
  assert(fs.existsSync(path.join(root, "store", row.asset)), `Missing asset for ${row.slug}: ${row.asset}`);
  assert(previewJs.includes(`${row.slug}:`) || previewJs.includes(`"${row.slug}":`), `Missing preview data for ${row.slug}`);
}

for (const row of catalogueRows) {
  assert(slugs.has(row.slug), `catalogue.csv contains slug not present in app-index.csv: ${row.slug}`);
}

const cardTitles = [...indexHtml.matchAll(/<h3>([^<]+)<\/h3>/g)].map((match) => match[1]);
for (const row of indexRows.filter((item) => item.slug !== "archive")) {
  assert(cardTitles.includes(row.title), `Store page is missing a card title for ${row.title}`);
}

for (const tag of tagSet) {
  assert(indexHtml.includes(`data-filter="${tag}"`), `Store page is missing filter button for ${tag}`);
  assert(
    indexHtml.includes(`href="?filter=${tag}#project-grid-heading"`),
    `Shelf link for ${tag} should work as a no-JS jump to the project grid`
  );
}

assert(indexHtml.includes('class="no-js"'), "Store HTML should start with a no-js class for progressive enhancement");
assert(indexHtml.includes("js-enabled"), "Store HTML should switch to js-enabled when scripts run");
assert(previewHtml.includes('class="no-js"'), "Preview HTML should start with a no-js class for progressive enhancement");
assert(previewHtml.includes("<noscript>"), "Preview page should include a no-JS fallback");
assert(indexHtml.includes('class="store-toolbar js-only"'), "Search/sort toolbar should be hidden when JS is disabled");
assert(indexHtml.includes('class="filters js-only"'), "Filter toolbar should be hidden when JS is disabled");
assert(storeCss.includes(".no-js .js-only"), "CSS should hide JS-only controls without JavaScript");
assert(storeScript.includes("#project-grid-heading"), "Shelf filtering should scroll to the project grid heading");

for (const file of requiredSpecFiles) {
  const absolutePath = path.join(root, file);
  assert(fs.existsSync(absolutePath), `Missing Spec Kit artifact: ${file}`);
  const contents = readFile(file);
  assert(!contents.includes("[NEEDS CLARIFICATION]"), `Unresolved clarification marker in ${file}`);
}

const constitution = readFile(".specify/memory/constitution.md");
assert(
  constitution.includes("Progressive enhancement is mandatory"),
  "Constitution must preserve the browser compatibility principle"
);

const spec = readFile(`${specDirectory}/spec.md`);
assert(spec.includes("Story 2: Navigate by category"), "Feature spec must cover category navigation");
assert(spec.includes("Story 3: Use previews safely"), "Feature spec must cover preview fallback behavior");

const tasks = readFile(`${specDirectory}/tasks.md`);
const uncheckedTasks = [...tasks.matchAll(/^- \[ \] /gm)];
assert(uncheckedTasks.length === 0, "Spec task list contains unchecked tasks");

console.log(`Validated ${indexRows.length} indexed store entries and ${tagRows.length} shelves.`);
