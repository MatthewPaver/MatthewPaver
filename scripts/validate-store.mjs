import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const requiredColumns = [
  "slug",
  "title",
  "shelf",
  "status",
  "kind",
  "problem",
  "proof",
  "stack",
  "preview",
  "asset",
  "solves",
  "shows"
];
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
const siteBase = "https://matthewpaver.github.io/MatthewPaver";

function readFile(relativePath) {
  return fs.readFileSync(path.join(root, relativePath), "utf8");
}

function readBuffer(relativePath) {
  return fs.readFileSync(path.join(root, relativePath));
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
  if (!condition) throw new Error(message);
}

function pngDimensions(buffer) {
  const signature = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
  for (let i = 0; i < signature.length; i += 1) {
    if (buffer[i] !== signature[i]) return null;
  }
  const width = buffer.readUInt32BE(16);
  const height = buffer.readUInt32BE(20);
  return { width, height };
}

function findImageTags(html) {
  const tags = [];
  const regex = /<img\b[^>]*?>/g;
  let match;
  while ((match = regex.exec(html)) !== null) {
    const tag = match[0];
    const src = /\bsrc=["']([^"']+)["']/.exec(tag)?.[1];
    const width = /\bwidth=["'](\d+)["']/.exec(tag)?.[1];
    const height = /\bheight=["'](\d+)["']/.exec(tag)?.[1];
    if (src) tags.push({ src, width: width ? Number(width) : null, height: height ? Number(height) : null });
  }
  return tags;
}

const indexRows = parseCsv(readFile("store/app-index.csv"));
const tagRows = parseCsv(readFile("store/tags.csv"));
const indexHtml = readFile("store/index.html");
const previewHtml = readFile("store/preview.html");
const previews = JSON.parse(readFile("store/previews.json"));
const storeScript = readFile("store/script.js");
const storeCss = readFile("store/styles.css");
const robots = readFile("robots.txt");
const sitemap = readFile("sitemap.xml");
const manifest = JSON.parse(readFile("store/manifest.webmanifest"));

const slugs = new Set();
const tagSet = new Set(tagRows.map((row) => row.tag));

assert(indexRows.length >= 10, "store/app-index.csv should include the full project catalogue");
assert(tagRows.length >= 6, "store/tags.csv should include the store shelves");
assert(!fs.existsSync(path.join(root, "store/catalogue.csv")), "store/catalogue.csv was removed in favour of app-index.csv");

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
  assert(previews[row.slug], `Missing previews.json entry for ${row.slug}`);
  assert(previews[row.slug].title, `previews.json entry for ${row.slug} lacks a title`);
  assert(previews[row.slug].image, `previews.json entry for ${row.slug} lacks an image`);
  assert(Array.isArray(previews[row.slug].links) && previews[row.slug].links.length > 0, `previews.json entry for ${row.slug} lacks links`);
}

const previewSlugs = Object.keys(previews);
for (const slug of previewSlugs) {
  assert(slugs.has(slug), `previews.json contains slug not present in app-index.csv: ${slug}`);
}

// Card title + data attribute parity
const articleRegex = /<article\b([^>]*?)class="app-card[^"]*"([^>]*?)>([\s\S]*?)<\/article>/g;
const cardMatches = [...indexHtml.matchAll(articleRegex)];
const cardsBySlug = new Map();
for (const match of cardMatches) {
  const openingAttrs = `${match[1]} ${match[2]}`;
  const slug = /data-slug=["']([^"']+)["']/.exec(openingAttrs)?.[1];
  const solves = /data-solves=["']([^"']+)["']/.exec(openingAttrs)?.[1];
  const shows = /data-shows=["']([^"']+)["']/.exec(openingAttrs)?.[1];
  const title = /<h3>([^<]+)<\/h3>/.exec(match[3])?.[1];
  if (slug) cardsBySlug.set(slug, { solves, shows, title });
}

for (const row of indexRows) {
  const card = cardsBySlug.get(row.slug);
  assert(card, `Store page is missing a card for slug ${row.slug}`);
  assert(card.title === row.title, `Card title mismatch for ${row.slug}: card has "${card.title}", CSV has "${row.title}"`);
  assert(card.solves === row.solves, `data-solves mismatch for ${row.slug}: card has "${card.solves}", CSV has "${row.solves}"`);
  assert(card.shows === row.shows, `data-shows mismatch for ${row.slug}: card has "${card.shows}", CSV has "${row.shows}"`);
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
assert(storeCss.includes("@media print"), "CSS should include a print stylesheet");
assert(storeCss.includes("@media (prefers-color-scheme: dark)"), "CSS should include a dark-mode block");
assert(storeScript.includes("#project-grid-heading"), "Shelf filtering should scroll to the project grid heading");
assert(storeScript.includes("searchIndex"), "Search should use a pre-computed index rather than reading textContent each keystroke");

// SEO + meta hygiene
assert(indexHtml.includes('rel="canonical"'), "Store HTML should declare a canonical URL");
assert(previewHtml.includes('rel="canonical"'), "Preview HTML should declare a canonical URL");
assert(indexHtml.includes('application/ld+json'), "Store HTML should embed JSON-LD structured data");
assert(indexHtml.includes('rel="preload"') && indexHtml.includes('as="image"'), "Store HTML should preload the LCP image");

const fetchPriorityHigh = (indexHtml.match(/fetchpriority="high"/g) || []).length;
assert(
  fetchPriorityHigh <= 2,
  `Only the preload + LCP image should use fetchpriority="high" (found ${fetchPriorityHigh})`
);

assert(indexHtml.includes('rel="manifest"'), "Store HTML should link the web manifest");
assert(indexHtml.includes('apple-touch-icon'), "Store HTML should link an apple-touch-icon");
assert(indexHtml.includes('http-equiv="Content-Security-Policy"'), "Store HTML should declare a CSP meta tag");
assert(previewHtml.includes('http-equiv="Content-Security-Policy"'), "Preview HTML should declare a CSP meta tag");

// Favicon + manifest assets
const requiredAssets = [
  "store/assets/favicon.svg",
  "store/assets/favicon-dark.svg",
  "store/assets/apple-touch-icon.svg",
  "store/assets/og-image.png",
  "store/manifest.webmanifest"
];
for (const asset of requiredAssets) {
  assert(fs.existsSync(path.join(root, asset)), `Missing required asset: ${asset}`);
}
assert(manifest.name && manifest.icons?.length, "manifest.webmanifest must declare a name and icons");

// PNG declared vs real dimensions
const imageTags = findImageTags(indexHtml).concat(findImageTags(previewHtml));
for (const tag of imageTags) {
  if (!tag.src.endsWith(".png")) continue;
  if (!tag.width || !tag.height) continue;
  const cleanPath = tag.src.replace(/^\.\//, "").replace(/^\//, "");
  const assetPath = cleanPath.startsWith("store/") ? cleanPath : `store/${cleanPath}`;
  const abs = path.join(root, assetPath);
  if (!fs.existsSync(abs)) continue;
  const dims = pngDimensions(readBuffer(assetPath));
  if (!dims) continue;
  assert(
    dims.width === tag.width && dims.height === tag.height,
    `Image dimension mismatch for ${tag.src}: declared ${tag.width}x${tag.height}, actual ${dims.width}x${dims.height}`
  );
}

// Sitemap covers every catalogue slug
for (const row of indexRows) {
  const url = `${siteBase}/store/preview.html?app=${row.slug}`;
  assert(sitemap.includes(url), `sitemap.xml is missing entry for ${url}`);
}
assert(sitemap.includes(`${siteBase}/store/`), "sitemap.xml must include the store root");

// robots.txt points to actual sitemap
assert(robots.includes(`Sitemap: ${siteBase}/sitemap.xml`), "robots.txt Sitemap line must point to /MatthewPaver/sitemap.xml");

// Spec artifacts
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

console.log(
  `Validated ${indexRows.length} indexed store entries, ${tagRows.length} shelves, ${previewSlugs.length} previews, ${imageTags.length} image tags.`
);
