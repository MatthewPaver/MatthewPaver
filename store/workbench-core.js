const LABEL_ALIASES = new Map([
  ["done", "done"],
  ["completed", "done"],
  ["progress", "done"],
  ["blocker", "blockers"],
  ["blocked", "blockers"],
  ["risk", "risks"],
  ["decision", "decisions"],
  ["next", "next"],
  ["metric", "metrics"],
  ["open", "open"],
  ["owner", "owners"],
  ["due", "due"],
  ["where", "where"],
  ["link", "where"],
]);

export function parseLabelledLines(text) {
  return String(text)
    .split(/\r?\n/)
    .map((line, index) => {
      const source = line.trim();
      if (!source) return null;
      const match = source.match(/^([A-Za-z ]{2,18}):\s*(.+)$/);
      if (!match) {
        return { type: "unlabelled", value: source, source, line: index + 1 };
      }
      const label = match[1].trim().toLowerCase();
      return {
        type: LABEL_ALIASES.get(label) || "unlabelled",
        value: match[2].trim(),
        source,
        line: index + 1,
      };
    })
    .filter(Boolean);
}

export function buildWeeklyUpdate(text) {
  const items = parseLabelledLines(text);
  const sections = [
    ["done", "Progress"],
    ["blockers", "Blockers"],
    ["decisions", "Decisions needed"],
    ["next", "Next"],
    ["metrics", "Measures"],
  ].map(([type, title]) => ({
    type,
    title,
    items: items.filter((item) => item.type === type),
  }));

  return {
    title: "Weekly update",
    sections,
    unlabelled: items.filter((item) => item.type === "unlabelled"),
    sourceCount: items.length,
  };
}

export function buildHandover(text) {
  const items = parseLabelledLines(text);
  const sections = [
    ["open", "Open work"],
    ["owners", "Owners"],
    ["due", "Due dates"],
    ["risks", "Risks"],
    ["where", "Where to find things"],
    ["next", "First next steps"],
  ].map(([type, title]) => ({
    type,
    title,
    items: items.filter((item) => item.type === type),
  }));

  return {
    title: "Handover",
    sections,
    unlabelled: items.filter((item) => item.type === "unlabelled"),
    sourceCount: items.length,
  };
}

function lcsMatrix(before, after) {
  const matrix = Array.from({ length: before.length + 1 }, () =>
    Array(after.length + 1).fill(0)
  );
  for (let i = before.length - 1; i >= 0; i -= 1) {
    for (let j = after.length - 1; j >= 0; j -= 1) {
      matrix[i][j] =
        before[i] === after[j]
          ? matrix[i + 1][j + 1] + 1
          : Math.max(matrix[i + 1][j], matrix[i][j + 1]);
    }
  }
  return matrix;
}

export function compareVersions(beforeText, afterText) {
  const before = String(beforeText)
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
  const after = String(afterText)
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
  const matrix = lcsMatrix(before, after);
  const changes = [];
  let i = 0;
  let j = 0;

  while (i < before.length && j < after.length) {
    if (before[i] === after[j]) {
      changes.push({ type: "unchanged", value: before[i] });
      i += 1;
      j += 1;
    } else if (matrix[i + 1][j] >= matrix[i][j + 1]) {
      changes.push({ type: "removed", value: before[i], line: i + 1 });
      i += 1;
    } else {
      changes.push({ type: "added", value: after[j], line: j + 1 });
      j += 1;
    }
  }
  while (i < before.length) {
    changes.push({ type: "removed", value: before[i], line: i + 1 });
    i += 1;
  }
  while (j < after.length) {
    changes.push({ type: "added", value: after[j], line: j + 1 });
    j += 1;
  }

  return {
    title: "Change summary",
    changes,
    added: changes.filter((change) => change.type === "added"),
    removed: changes.filter((change) => change.type === "removed"),
    unchanged: changes.filter((change) => change.type === "unchanged"),
  };
}

export function resultToMarkdown(result) {
  if (result.changes) {
    const lines = [
      `# ${result.title}`,
      "",
      `Added: ${result.added.length} · Removed: ${result.removed.length} · Unchanged: ${result.unchanged.length}`,
      "",
      "## Added",
      ...result.added.map((item) => `- ${item.value}`),
      "",
      "## Removed",
      ...result.removed.map((item) => `- ${item.value}`),
    ];
    return lines.join("\n");
  }

  const lines = [`# ${result.title}`, ""];
  result.sections.forEach((section) => {
    lines.push(`## ${section.title}`);
    if (!section.items.length) lines.push("- Not provided");
    section.items.forEach((item) => lines.push(`- ${item.value} _(source line ${item.line})_`));
    lines.push("");
  });
  if (result.unlabelled.length) {
    lines.push("## Needs sorting");
    result.unlabelled.forEach((item) => lines.push(`- ${item.value} _(source line ${item.line})_`));
  }
  return lines.join("\n").trim();
}
