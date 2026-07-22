<!-- rtk-instructions v2 -->
# RTK — Token-Optimized CLI

**rtk** is a CLI proxy that filters and compresses command outputs, saving 60-90% tokens.

## Rule

Always prefix shell commands with `rtk`:

```bash
# Instead of:              Use:
git status                 rtk git status
git log -10                rtk git log -10
cargo test                 rtk cargo test
docker ps                  rtk docker ps
kubectl get pods           rtk kubectl pods
```

## Meta commands (use directly)

```bash
rtk gain              # Token savings dashboard
rtk gain --history    # Per-command savings history
rtk discover          # Find missed rtk opportunities
rtk proxy <cmd>       # Run raw (no filtering) but track usage
```
<!-- /rtk-instructions -->

## Build, test, and lint commands

This repository has no single root build/test/lint pipeline. Run commands from `Work/Automações/Entregaveis` when validating automation changes.

### `Work/Automações/Entregaveis` (Python automation project)

```bash
# Install dependencies
python -m pip install -r requirements.txt

# Run integration tests
python -m unittest _dev/test_integration.py

# Run a single test by pattern
python -m unittest _dev/test_integration.py -k test_get_dashboard

# Main report generation flow (from project docs)
uv run python gerar_apresentacao.py --cliente CLIENTE --data-inicio YYYY-MM-DD --data-fim YYYY-MM-DD
```

## High-level architecture

### 1) Knowledge-base layer (repository root)
- The repository is primarily a Markdown knowledge base published through a GitBook-style structure.
- `SUMMARY.md` is the canonical table of contents for published navigation; structural content changes must be reflected there.
- Content is distributed mainly across:
  - `readme-1/` (large, structured handbook tree)
  - `cyberetico/` (security/course notes and related materials)
  - `obsidian/` and `Work/` (workspace notes and operational documentation)

### 2) Automation layer (`Work/Automações/Entregaveis`)
- This is a Python pipeline for SOC/client deliverables and presentation generation.
- Main flow is split into:
  1. **Ingestion** (`app/api/ingestion.py`): pulls data from Grafana, Artia, Stellar Cyber, and Zammad.
  2. **Persistence** (`app/db/crud.py`): writes normalized data into PostgreSQL tables via generated CRUD/upsert functions based on `TABLE_SPECS`.
  3. **Payload + metrics assembly** (`app/presentation/generator.py`, `alert_metrics.py`): computes monthly metrics and placeholder values.
  4. **Presentation rendering** (`update_presentation.py`, `gerar_apresentacao.py`): replaces template placeholders/charts and writes PPTX outputs.

## Key conventions in this repository

### Markdown/content conventions
- Use YAML front matter on top-level/content index notes where present (for example root `README.md` and many section index pages).
- Internal links heavily use Obsidian wikilinks (`[[...]]`), including links across folders and generated overview files.
- Many overview files include generated `%% Begin Waypoint %%` / `%% End Waypoint %%` blocks; preserve these blocks when editing those files.
- Keep `SUMMARY.md` synchronized when pages are added, removed, renamed, or moved in the published tree.

### Automation conventions (`Work/Automações/Entregaveis`)
- Environment variables are loaded from `.env` with `.env.example` as reference; integrations should use existing setting keys from `app/config.py`.
- Ingestion functions return structured status payloads (`status`, `source`, `reason`/`error`, `persisted`) instead of raising broad failures for missing credentials.
- Database access should go through `app/db/crud.py` table APIs (`create_*`, `list_*`, `upsert_*`) instead of ad-hoc SQL in feature modules.
- Monthly metrics logic is month-key based (`YYYY-MM`) and uses current-vs-previous month comparisons across ingestion and presentation modules; preserve this pattern when extending metrics.

### Existing assistant-governance files to respect
- `.github/AGENTS.md` and `.github/CLAUDE.md` define SDD/handoff workflow expectations used by this repo’s agent setup.
- The RTK rule above is duplicated in root and `Work/.github/` and should be treated as standard for shell command examples.
