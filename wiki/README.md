# Portfolio Wiki Schema

This folder follows the Karpathy-style LLM wiki pattern in a lightweight way: source files stay separate, and the working knowledge is compiled into linked Markdown pages that can be maintained over time.

## Folder Rules

| Layer | Path | Rule |
|:---|:---|:---|
| Raw/source register | `wiki/raw/` | Keep source pointers here. Do not rewrite canonical source files through the wiki. |
| Compiled wiki pages | `wiki/pages/` | Maintain durable summaries, project maps, decisions, and quality-gate notes. |
| Index | `wiki/index.md` | Keep this as the main entry point. Link every compiled page here. |
| Log | `wiki/log.md` | Record meaningful ingest, audit, and maintenance passes. |

## Update Workflow

1. Read the canonical source files listed in `wiki/raw/source-register.md`.
2. Update the relevant page in `wiki/pages/`.
3. Add or refresh links in `wiki/index.md`.
4. Record the change in `wiki/log.md`.
5. Run `npm run audit:portfolio`.

## Ownership

The wiki is allowed to summarise and cross-link the portfolio. It should not become the front door. The front door remains `README.md` and the visual store remains `store/index.html`.
