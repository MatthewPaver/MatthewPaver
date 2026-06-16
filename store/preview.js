const SITE_BASE = "https://matthewpaver.github.io/MatthewPaver/store/";

function setText(id, text) {
  const node = document.querySelector(`#${id}`);
  if (node) node.textContent = text;
}

function setMeta(selector, attribute, value) {
  const node = document.querySelector(selector);
  if (node) node.setAttribute(attribute, value);
}

function updateSocialMeta(preview, slug) {
  const absoluteImage = preview.image.replace(/^\.\//, SITE_BASE);
  const previewUrl = `${SITE_BASE}preview.html?app=${slug}`;
  const title = `${preview.title} · Matthew Paver Portfolio Store`;

  document.title = title;
  setMeta("meta[name='description']", "content", preview.summary);
  setMeta("meta[property='og:title']", "content", title);
  setMeta("meta[property='og:description']", "content", preview.summary);
  setMeta("meta[property='og:url']", "content", previewUrl);
  setMeta("meta[property='og:image']", "content", absoluteImage);
  setMeta("meta[property='og:image:alt']", "content", preview.imageAlt);
  setMeta("meta[name='twitter:title']", "content", title);
  setMeta("meta[name='twitter:description']", "content", preview.summary);
  setMeta("meta[name='twitter:image']", "content", absoluteImage);
  setMeta("link[rel='canonical']", "href", previewUrl);
}

function renderUnknown(slug) {
  document.title = "Unknown app · Matthew Paver Portfolio Store";
  setText("preview-kicker", "Not found");
  setText("preview-title", `No preview for “${slug}”`);
  setText(
    "preview-summary",
    "That preview slug is not in the store catalogue. The project may have been renamed or archived. Head back to browse every project."
  );

  const media = document.querySelector(".preview-media");
  if (media) media.hidden = true;

  const layout = document.querySelector(".preview-layout");
  if (layout) layout.hidden = true;

  const actions = document.querySelector("#preview-actions");
  if (actions) {
    const back = document.createElement("a");
    back.className = "button primary";
    back.href = "./";
    back.textContent = "Back to store";
    actions.replaceChildren(back);
  }
}

function renderPreview(preview, slug) {
  updateSocialMeta(preview, slug);
  setText("preview-kicker", preview.kicker);
  setText("preview-title", preview.title);
  setText("preview-summary", preview.summary);
  setText("preview-role", preview.role);
  setText("preview-status", preview.status);
  setText("preview-focus", preview.focus);
  setText("preview-problem", preview.problem);
  setText("preview-note", preview.note);

  const image = document.querySelector("#preview-image");
  const imageAvif = document.querySelector("#preview-image-avif");
  const video = document.querySelector("#preview-video");
  const picture = document.querySelector("#preview-picture");
  if (imageAvif) {
    if (preview.imageAvif) {
      imageAvif.srcset = preview.imageAvif;
    } else {
      imageAvif.removeAttribute("srcset");
    }
  }

  if (image) {
    image.src = preview.image;
    image.alt = preview.imageAlt;
    image.hidden = Boolean(preview.video);
  }

  if (picture) {
    picture.hidden = Boolean(preview.video);
  }

  if (video) {
    if (preview.video) {
      video.src = preview.video;
      video.poster = preview.image;
      video.hidden = false;
      video.setAttribute("aria-label", `${preview.title} demo video`);
    } else {
      video.removeAttribute("src");
      video.removeAttribute("poster");
      video.hidden = true;
      video.removeAttribute("aria-label");
    }
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

async function init() {
  const params = new URLSearchParams(window.location.search);
  const slug = params.get("app") || "inference";

  try {
    const response = await fetch("./previews.json", { cache: "no-cache" });
    if (!response.ok) throw new Error(`previews.json ${response.status}`);
    const previews = await response.json();
    const preview = previews[slug];

    if (!preview) {
      renderUnknown(slug);
      return;
    }

    renderPreview(preview, slug);
  } catch (error) {
    console.error("Failed to load previews.json", error);
    renderUnknown(slug);
  }
}

document.addEventListener("DOMContentLoaded", init);
