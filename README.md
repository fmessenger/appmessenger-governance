# appmessenger-governance

Governance scaffold for AppMessenger.

- Source of truth backlog: `backlog/backlog.csv` (26 columns, strict order).
- Docs-as-code: Markdown with YAML headers under `docs/`.
- CI (Continuous Integration): `.github/workflows/traceability.yml` validates traceability and builds exports (XLSX/PNG/PDF).
- Artifacts are uploaded on each Pull Request (PR) and push to `main`.

## Workflow
1. Edit `backlog/backlog.csv` and docs under `docs/*` in a feature branch.
2. Open a PR. CI runs validation and exports.
3. Review on iPhone (GitHub Mobile), then Approve & Merge.
