import fs from "node:fs";

const canonicalStore = "https://matthewpaver.github.io/";
const storeHtml = fs.readFileSync("store/index.html", "utf8");
const previewHtml = fs.readFileSync("store/preview.html", "utf8");

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

assert(
  storeHtml.includes(`rel="canonical" href="${canonicalStore}"`),
  "Legacy store must identify the root product store as canonical",
);
assert(
  storeHtml.includes(`window.location.replace("${canonicalStore}")`),
  "Legacy store must redirect visitors to the root product store",
);
assert(
  storeHtml.includes('name="robots" content="noindex,follow"'),
  "Legacy store must not compete with the canonical store in search",
);
assert(
  previewHtml.includes('name="robots" content="noindex,follow"'),
  "Legacy preview routes must remain out of the search index",
);

for (const slug of [
  "meetingproof",
  "projectlens",
  "decisiongraph",
  "happening",
  "quicksupply",
  "marketing-ml-lakehouse",
]) {
  assert(
    previewHtml.includes(`"${slug}"`),
    `Legacy preview redirect is missing the ${slug} destination`,
  );
}

console.log("Legacy store redirects point to the canonical product store.");
