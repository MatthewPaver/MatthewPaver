import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const targets = ["store/index.html", "store/preview.html"];
const pattern = /(\?v=)([0-9]{8}-[0-9]+)/g;

const today = new Date().toISOString().slice(0, 10).replace(/-/g, "");
const explicit = process.argv[2];

let nextToken = explicit;
if (!nextToken) {
  const seen = new Set();
  for (const file of targets) {
    const text = fs.readFileSync(path.join(root, file), "utf8");
    for (const match of text.matchAll(pattern)) {
      seen.add(match[2]);
    }
  }
  const datePrefix = today;
  let highestSerial = 0;
  for (const token of seen) {
    const [date, serial] = token.split("-");
    if (date === datePrefix) highestSerial = Math.max(highestSerial, Number(serial));
  }
  nextToken = `${datePrefix}-${highestSerial + 1}`;
}

if (!/^[0-9]{8}-[0-9]+$/.test(nextToken)) {
  console.error(`Invalid token "${nextToken}". Expected YYYYMMDD-N.`);
  process.exit(1);
}

let changed = 0;
for (const file of targets) {
  const absolute = path.join(root, file);
  const original = fs.readFileSync(absolute, "utf8");
  const updated = original.replace(pattern, `$1${nextToken}`);
  if (updated !== original) {
    fs.writeFileSync(absolute, updated);
    changed += 1;
  }
}

console.log(`Bumped cache token to ${nextToken} across ${changed} file(s).`);
