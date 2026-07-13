import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const auditDir = "tools/portfolio-audit";
const benchmarks = JSON.parse(readFile(`${auditDir}/benchmarks.json`));
const outputPath = path.join(root, "PORTFOLIO_AUDIT.md");

function readFile(relativePath) {
  return fs.readFileSync(path.join(root, relativePath), "utf8");
}

function readBuffer(relativePath) {
  return fs.readFileSync(path.join(root, relativePath));
}

function exists(relativePath) {
  return fs.existsSync(path.join(root, relativePath));
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

function pngDimensions(buffer) {
  const signature = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
  if (!signature.every((byte, index) => buffer[index] === byte)) return null;
  return { width: buffer.readUInt32BE(16), height: buffer.readUInt32BE(20), kind: "png" };
}

function gifDimensions(buffer) {
  const header = buffer.subarray(0, 6).toString("ascii");
  if (header !== "GIF87a" && header !== "GIF89a") return null;
  return { width: buffer.readUInt16LE(6), height: buffer.readUInt16LE(8), kind: "gif" };
}

function jpegDimensions(buffer) {
  if (buffer[0] !== 0xff || buffer[1] !== 0xd8) return null;

  let offset = 2;
  while (offset < buffer.length) {
    if (buffer[offset] !== 0xff) return null;
    const marker = buffer[offset + 1];
    const length = buffer.readUInt16BE(offset + 2);

    if (marker >= 0xc0 && marker <= 0xc3) {
      return {
        width: buffer.readUInt16BE(offset + 7),
        height: buffer.readUInt16BE(offset + 5),
        kind: "jpeg"
      };
    }

    offset += 2 + length;
  }

  return null;
}

function svgDimensions(text) {
  const viewBox = /viewBox=["']([^"']+)["']/.exec(text)?.[1]?.split(/\s+/).map(Number);
  if (viewBox?.length === 4 && viewBox.every(Number.isFinite)) {
    return { width: viewBox[2], height: viewBox[3], kind: "svg" };
  }

  const width = /width=["'](\d+(?:\.\d+)?)/.exec(text)?.[1];
  const height = /height=["'](\d+(?:\.\d+)?)/.exec(text)?.[1];
  if (width && height) return { width: Number(width), height: Number(height), kind: "svg" };
  return null;
}

function assetDimensions(relativePath) {
  const cleanPath = relativePath.replace(/^\.\//, "").replace(/^store\//, "store/");
  const fullPath = cleanPath.startsWith("store/") ? cleanPath : `store/${cleanPath}`;
  if (!exists(fullPath)) return null;

  const buffer = readBuffer(fullPath);
  if (fullPath.endsWith(".png")) return pngDimensions(buffer) || jpegDimensions(buffer);
  if (fullPath.endsWith(".gif")) return gifDimensions(buffer);
  if (fullPath.endsWith(".svg")) return svgDimensions(readFile(fullPath));
  return null;
}

function countMatches(text, regex) {
  return [...text.matchAll(regex)].length;
}

function addFinding(findings, agent, severity, message, fix) {
  findings.push({ agent, severity, message, fix });
}

function score(findings) {
  const penalty = findings.reduce((total, finding) => {
    if (finding.severity === "high") return total + 9;
    if (finding.severity === "medium") return total + 4;
    return total + 1;
  }, 0);
  return Math.max(0, 100 - penalty);
}

function severityWeight(severity) {
  return { high: 0, medium: 1, low: 2 }[severity] ?? 3;
}

function inspectReadme(readme, findings) {
  const badgeCount = countMatches(readme, /img\.shields\.io/g);
  const sectionCount = countMatches(readme, /^## /gm);
  const detailsCount = countMatches(readme, /<details>/g);

  if (!readme.includes("Featured products")) {
    addFinding(findings, "README agent", "high", "The README should expose the strongest work before secondary detail.", "Keep Featured products near the top.");
  }

  if (!readme.includes("Portfolio Store")) {
    addFinding(findings, "README agent", "high", "The profile should route quickly into the visual store.", "Keep a prominent Portfolio Store badge/link.");
  }

  if (badgeCount > 26) {
    addFinding(findings, "README slop detector", "medium", `The README has ${badgeCount} badge/image badge references, which can start to feel template-heavy.`, "Keep top badges and project proof badges, but avoid a badge wall.");
  }

  if (sectionCount > 12) {
    addFinding(findings, "README agent", "medium", `The README has ${sectionCount} top-level sections.`, "Push detailed reference material into Projects.md or the store.");
  }

  if (detailsCount === 0) {
    addFinding(findings, "README agent", "low", "The README has no collapsed maintenance/reference block.", "Keep auto-updated or long reference material inside details.");
  }

  const presentationDrift = [
    ["## Latest shipping", "A dated shipping table goes stale quickly."],
    ["## Portfolio quality gates", "Portfolio maintenance details are competing with the work."],
    ["## GitHub signals", "Generic GitHub stat cards add little project evidence."],
    ["## Shortcuts", "The shortcuts repeat links already exposed above."]
  ];

  for (const [heading, message] of presentationDrift) {
    if (readme.includes(heading)) {
      addFinding(findings, "README agent", "medium", message, `Remove ${heading.replace("## ", "")} from the public profile.`);
    }
  }

  if (/store\/assets\/[\w-]+\.gif/.test(readme)) {
    addFinding(findings, "README agent", "medium", "Animated project previews make the profile busy and can move too quickly.", "Use calm, representative screenshots in the profile and keep video on preview pages.");
  }

  for (const phrase of benchmarks.slopPhrases) {
    const regex = new RegExp(phrase.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "i");
    if (regex.test(readme)) {
      addFinding(findings, "README slop detector", "low", `Potential generic phrase in README: "${phrase}".`, "Replace with a concrete project detail or remove it.");
    }
  }
}

function inspectPortfolioContracts(indexHtml, findings) {
  const rootIndex = readFile("index.html");
  const pagesWorkflow = readFile(".github/workflows/pages.yml");
  const contract = readFile("specs/001-portfolio-store-reliability/contracts/store-catalogue.md");
  const preload = indexHtml.match(/rel="preload"[^>]+href="\.\/assets\/([^"]+)"/)?.[1];

  if (rootIndex.includes("Idea Store")) {
    addFinding(findings, "catalogue agent", "low", "The root redirect still calls the site the Idea Store.", "Use Portfolio Store consistently across the redirect and catalogue.");
  }

  if (pagesWorkflow.includes("Idea Store")) {
    addFinding(findings, "catalogue agent", "low", "The Pages workflow still uses the old Idea Store name.", "Use Portfolio Store consistently in Actions and on the deployed site.");
  }

  if (preload && !contract.includes(`\`${preload}\``)) {
    addFinding(findings, "catalogue agent", "medium", `The SEO contract does not name the current LCP preload (${preload}).`, "Keep the written contract aligned with the deployed preload asset.");
  }
}

function inspectStore(indexHtml, rows, previews, findings) {
  const cardCount = countMatches(indexHtml, /class="app-card/g);
  const previewLinkCount = countMatches(indexHtml, /preview\.html\?app=/g);
  const archiveRows = rows.filter((row) => row.shelf === "archive");
  const publicRows = rows.filter((row) => row.status.toLowerCase().includes("public"));

  if (cardCount !== rows.length) {
    addFinding(findings, "catalogue agent", "high", `Store has ${cardCount} cards but app-index.csv has ${rows.length} rows.`, "Keep card markup and catalogue rows in sync.");
  }

  if (previewLinkCount < rows.length) {
    addFinding(findings, "catalogue agent", "medium", "Not every catalogue item appears to link to a preview page.", "Give every project an app-store style preview.");
  }

  if (archiveRows.length > 2) {
    addFinding(findings, "catalogue agent", "medium", "Archive projects are starting to compete with current work.", "Keep archive items behind the archive filter or footer.");
  }

  for (const row of rows) {
    if (!previews[row.slug]) {
      addFinding(findings, "catalogue agent", "high", `${row.title} is missing a preview entry.`, "Add it to store/previews.json.");
    }

    const dimensions = assetDimensions(row.asset);
    if (!dimensions) {
      addFinding(findings, "thumbnail QA agent", "high", `${row.title} asset cannot be inspected: ${row.asset}.`, "Check the asset path and file type.");
      continue;
    }

    const ratio = dimensions.width / dimensions.height;
    if (ratio < 1.25 || ratio > 2.05) {
      addFinding(
        findings,
        "thumbnail QA agent",
        "medium",
        `${row.title} thumbnail is ${dimensions.width}x${dimensions.height}, which may crop awkwardly in app-store cards.`,
        "Prefer 16:9 or 3:2 thumbnails with quiet margins."
      );
    }

    if (row.asset.endsWith(".svg") && ["product", "data", "analytics"].includes(row.shelf)) {
      addFinding(
        findings,
        "thumbnail QA agent",
        "low",
        `${row.title} still uses an SVG/diagram-style thumbnail.`,
        "Use a real or sanitised product screenshot when possible."
      );
    }
  }

  for (const row of publicRows) {
    const htmlSlice = indexHtml.match(new RegExp(`<article[^>]+data-slug=["']${row.slug}["'][\\s\\S]*?<\\/article>`))?.[0] || "";
    if (!htmlSlice.includes("repo-confidence")) {
      addFinding(findings, "repo packaging agent", "medium", `${row.title} is public but lacks repo-confidence signals on the card.`, "Show Open repo, tests, demo data, or run-locally where true.");
    }
  }
}

function inspectRepoPackaging(rows, findings) {
  const publicRows = rows.filter((row) => row.repo);
  for (const row of publicRows) {
    if (!row.repo.includes("github.com/MatthewPaver/")) continue;
    if (!row.problem || !row.proof || !row.stack) {
      addFinding(findings, "repo packaging agent", "medium", `${row.title} catalogue metadata is too thin.`, "Keep problem, proof, and stack populated.");
    }
  }
}

function inspectAppIdeas(findings) {
  const ideaFile = "APP_IDEAS.md";
  if (!exists(ideaFile)) {
    addFinding(findings, "ideas agent", "medium", "There is no tracked backlog of portfolio-grade app ideas.", "Add APP_IDEAS.md with ideas ranked by portfolio value.");
  }
}

function inspectWikiPattern(findings) {
  const requiredWikiFiles = [
    "wiki/README.md",
    "wiki/index.md",
    "wiki/log.md",
    "wiki/raw/source-register.md",
    "wiki/pages/portfolio-system.md",
    "wiki/pages/project-catalogue.md",
    "wiki/pages/quality-gates.md"
  ];

  for (const file of requiredWikiFiles) {
    if (!exists(file)) {
      addFinding(findings, "Karpathy wiki agent", "medium", `Missing wiki-pattern file: ${file}.`, "Keep raw sources, compiled wiki pages, index, and log in the repo.");
    }
  }

  if (!requiredWikiFiles.every(exists)) return;

  const schema = readFile("wiki/README.md");
  const index = readFile("wiki/index.md");
  const log = readFile("wiki/log.md");
  const sourceRegister = readFile("wiki/raw/source-register.md");
  const pageFiles = requiredWikiFiles.filter((file) => file.startsWith("wiki/pages/"));

  for (const principle of benchmarks.wikiPatternPrinciples) {
    const keyword = principle.split(" ")[1]?.toLowerCase();
    if (keyword && !schema.toLowerCase().includes(keyword)) {
      addFinding(findings, "Karpathy wiki agent", "low", `Wiki schema may not explicitly cover: ${principle}`, "Keep the wiki README as the schema for source, compile, index, and log rules.");
    }
  }

  for (const file of pageFiles) {
    const link = file.replace("wiki/", "");
    if (!index.includes(link)) {
      addFinding(findings, "Karpathy wiki agent", "medium", `wiki/index.md does not link to ${file}.`, "Keep the wiki index as the entry point for every compiled page.");
    }
  }

  for (const source of ["README.md", "store/app-index.csv", "store/previews.json", "CASE_STUDIES.md", "Projects.md"]) {
    if (!sourceRegister.includes(source)) {
      addFinding(findings, "Karpathy wiki agent", "low", `Source register does not mention ${source}.`, "List canonical source files in wiki/raw/source-register.md.");
    }
  }

  if (!log.includes("Portfolio audit agents") && !log.includes("Karpathy")) {
    addFinding(findings, "Karpathy wiki agent", "low", "wiki/log.md does not record the current portfolio-audit/wiki pass.", "Record notable ingest and maintenance passes in wiki/log.md.");
  }
}

function renderReport(findings, rows) {
  const ordered = [...findings].sort((a, b) => severityWeight(a.severity) - severityWeight(b.severity));
  const byAgent = Map.groupBy ? Map.groupBy(ordered, (finding) => finding.agent) : groupByAgent(ordered);
  const health = score(ordered);

  const lines = [
    "# Portfolio Audit",
    "",
    "Generated by: `npm run audit:portfolio`",
    "",
    `Health score: ${health}/100`,
    "",
    "This report is produced by deterministic portfolio review passes. It is designed to keep the profile and app store sharp without turning the page into a generic template.",
    "",
    "## Review Agents",
    "",
    "| Agent | What it checks |",
    "|:---|:---|",
    "| Research agent | Benchmarks the profile against strong GitHub/profile patterns without copying them. |",
    "| README agent | Keeps the profile lean, routed, and project-led. |",
    "| README slop detector | Flags generic phrases that make the writing sound generated. |",
    "| Thumbnail QA agent | Checks assets for missing files, awkward aspect ratios, and diagram-heavy cards. |",
    "| Catalogue agent | Checks store/card/preview consistency. |",
    "| Repo packaging agent | Checks whether public projects are presented with confidence. |",
    "| Ideas agent | Keeps a small backlog of portfolio-grade next builds. |",
    "| Karpathy wiki agent | Checks source/wiki separation, compiled pages, index, and maintenance log. |",
    "",
    "## Benchmark Notes",
    "",
    ...benchmarks.profileCollections.map((item) => `- ${item.name}: ${item.url} - ${item.useFor}`),
    "",
    "Karpathy wiki-pattern principles used by the audit:",
    "",
    ...benchmarks.wikiPatternPrinciples.map((principle) => `- ${principle}`),
    "",
    "## Findings",
    ""
  ];

  if (ordered.length === 0) {
    lines.push("No findings. The portfolio is in very good shape.", "");
  } else {
    for (const [agent, agentFindings] of byAgent.entries()) {
      lines.push(`### ${agent}`, "");
      for (const finding of agentFindings) {
        lines.push(`- ${finding.severity.toUpperCase()}: ${finding.message}`);
        lines.push(`  Fix: ${finding.fix}`);
      }
      lines.push("");
    }
  }

  lines.push("## Catalogue Snapshot", "");
  lines.push("| Shelf | Count |");
  lines.push("|:---|---:|");
  for (const [shelf, shelfRows] of groupByAgent(rows.map((row) => ({ agent: row.shelf }))).entries()) {
    lines.push(`| ${shelf} | ${shelfRows.length} |`);
  }

  lines.push("", "## Next Best Actions", "");
  const next = [];
  const seenFixes = new Set();
  for (const finding of ordered) {
    if (seenFixes.has(finding.fix)) continue;
    seenFixes.add(finding.fix);
    next.push(finding);
    if (next.length === 5) break;
  }
  if (next.length === 0) {
    lines.push("- Keep running `npm run audit:portfolio` before major profile/store changes.");
  } else {
    next.forEach((finding, index) => {
      lines.push(`${index + 1}. ${finding.fix}`);
    });
  }

  lines.push("", "## App Ideas", "");
  lines.push("See APP_IDEAS.md for the ranked backlog.");
  lines.push("");

  return lines.join("\n");
}

function groupByAgent(items) {
  const groups = new Map();
  for (const item of items) {
    if (!groups.has(item.agent)) groups.set(item.agent, []);
    groups.get(item.agent).push(item);
  }
  return groups;
}

const readme = readFile("README.md");
const indexHtml = readFile("store/index.html");
const rows = parseCsv(readFile("store/app-index.csv"));
const previews = JSON.parse(readFile("store/previews.json"));
const findings = [];

inspectReadme(readme, findings);
inspectStore(indexHtml, rows, previews, findings);
inspectPortfolioContracts(indexHtml, findings);
inspectRepoPackaging(rows, findings);
inspectAppIdeas(findings);
inspectWikiPattern(findings);

const report = renderReport(findings, rows);
fs.writeFileSync(outputPath, report);
console.log(report);
