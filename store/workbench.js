import {
  buildHandover,
  buildWeeklyUpdate,
  compareVersions,
  resultToMarkdown,
} from "./workbench-core.js";

const samples = {
  update: `Done: Supplier shortlist agreed with Finance
Done: Pilot team completed the first walkthrough
Blocker: Data-sharing approval is still waiting on Legal
Decision: Confirm whether the pilot includes the North region
Next: Priya to circulate the revised plan on Friday
Metric: 18 of 22 pilot users completed onboarding`,
  handover: `Open: Finalise the supplier onboarding checklist
Owner: Priya owns commercial queries; Dan owns access requests
Due: Pilot readiness review is 24 July
Risk: Two user accounts still need information-security approval
Where: Working files are in Teams / Project Cedar / 04 Delivery
Next: Check the approvals tracker before Tuesday's stand-up`,
  before: `Pilot launch: 29 July
Scope: London and South East teams
Training: one live session
Approval owner: Operations Director
Success measure: 70% weekly use`,
  after: `Pilot launch: 5 August
Scope: London, South East and North teams
Training: two live sessions plus a recording
Approval owner: Operations Director
Success measure: 80% weekly use`,
};

let latestResult = null;
let latestTool = "update";

const panels = Array.from(document.querySelectorAll("[data-tool-panel]"));
const tabs = Array.from(document.querySelectorAll("[data-tool-tab]"));
const output = document.querySelector("#workbench-output");
const outputTitle = document.querySelector("#output-title");
const outputState = document.querySelector("#output-state");
const exportButton = document.querySelector("#export-result");
const copyButton = document.querySelector("#copy-result");
const resetButton = document.querySelector("#reset-result");

function setActiveTool(name) {
  latestTool = name;
  tabs.forEach((tab) => {
    const active = tab.dataset.toolTab === name;
    tab.classList.toggle("active", active);
    tab.setAttribute("aria-selected", String(active));
    tab.tabIndex = active ? 0 : -1;
  });
  panels.forEach((panel) => {
    panel.hidden = panel.dataset.toolPanel !== name;
  });
  resetOutput();
  document.querySelector(`[data-tool-panel="${name}"] textarea`)?.focus();
}

function itemMarkup(item) {
  return `<li><span>${escapeHtml(item.value)}</span><small>Source line ${item.line}: “${escapeHtml(
    item.source
  )}”</small></li>`;
}

function renderStructured(result) {
  return result.sections
    .map(
      (section) => `<section class="result-section">
        <h4>${section.title}<span>${section.items.length}</span></h4>
        ${
          section.items.length
            ? `<ul>${section.items.map(itemMarkup).join("")}</ul>`
            : '<p class="missing-value">Not provided — add it before sending.</p>'
        }
      </section>`
    )
    .join("") +
    (result.unlabelled.length
      ? `<section class="result-section needs-review"><h4>Needs sorting<span>${result.unlabelled.length}</span></h4>
          <ul>${result.unlabelled.map(itemMarkup).join("")}</ul></section>`
      : "");
}

function renderDiff(result) {
  const renderList = (items, empty, marker) =>
    items.length
      ? `<ul>${items
          .map(
            (item) =>
              `<li><strong aria-hidden="true">${marker}</strong><span>${escapeHtml(
                item.value
              )}</span><small>Exact line from ${marker === "+" ? "new" : "old"} version</small></li>`
          )
          .join("")}</ul>`
      : `<p class="missing-value">${empty}</p>`;
  return `<div class="change-totals" aria-label="Change totals">
      <span><strong>${result.added.length}</strong> added</span>
      <span><strong>${result.removed.length}</strong> removed</span>
      <span><strong>${result.unchanged.length}</strong> unchanged</span>
    </div>
    <section class="result-section change-added"><h4>Added<span>${result.added.length}</span></h4>
      ${renderList(result.added, "Nothing added.", "+")}</section>
    <section class="result-section change-removed"><h4>Removed<span>${result.removed.length}</span></h4>
      ${renderList(result.removed, "Nothing removed.", "−")}</section>`;
}

function renderResult(result) {
  latestResult = result;
  outputTitle.textContent = result.title;
  outputState.textContent = "Draft ready — check it before sharing";
  outputState.classList.add("ready");
  output.innerHTML = result.changes ? renderDiff(result) : renderStructured(result);
  exportButton.disabled = false;
  copyButton.disabled = false;
  output.focus();
}

function resetOutput() {
  latestResult = null;
  outputTitle.textContent = "Your draft will appear here";
  outputState.textContent = "Nothing has been sent or saved";
  outputState.classList.remove("ready");
  output.innerHTML =
    '<div class="empty-output"><span aria-hidden="true">↳</span><p>Choose a tool, use the safe sample or paste your own text, then make a draft.</p></div>';
  exportButton.disabled = true;
  copyButton.disabled = true;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

tabs.forEach((tab) => tab.addEventListener("click", () => setActiveTool(tab.dataset.toolTab)));
document.querySelectorAll("[data-open-tool]").forEach((link) => {
  link.addEventListener("click", () => setActiveTool(link.dataset.openTool));
});

document.querySelector("#build-update").addEventListener("click", () => {
  renderResult(buildWeeklyUpdate(document.querySelector("#update-input").value));
});
document.querySelector("#build-handover").addEventListener("click", () => {
  renderResult(buildHandover(document.querySelector("#handover-input").value));
});
document.querySelector("#compare-change").addEventListener("click", () => {
  renderResult(
    compareVersions(
      document.querySelector("#before-input").value,
      document.querySelector("#after-input").value
    )
  );
});

document.querySelectorAll("[data-sample]").forEach((button) => {
  button.addEventListener("click", () => {
    const sample = button.dataset.sample;
    if (sample === "update") document.querySelector("#update-input").value = samples.update;
    if (sample === "handover") document.querySelector("#handover-input").value = samples.handover;
    if (sample === "change") {
      document.querySelector("#before-input").value = samples.before;
      document.querySelector("#after-input").value = samples.after;
    }
  });
});

copyButton.addEventListener("click", async () => {
  if (!latestResult) return;
  await navigator.clipboard.writeText(resultToMarkdown(latestResult));
  copyButton.textContent = "Copied";
  window.setTimeout(() => (copyButton.textContent = "Copy"), 1200);
});

exportButton.addEventListener("click", () => {
  if (!latestResult) return;
  const blob = new Blob([resultToMarkdown(latestResult)], { type: "text/markdown" });
  const href = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = href;
  link.download = `${latestTool}-draft.md`;
  link.click();
  URL.revokeObjectURL(href);
});

resetButton.addEventListener("click", resetOutput);
resetOutput();
