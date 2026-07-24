Title: chore(vault): consolidate Obsidian vault and add conventions

This PR consolidates the Obsidian vault and adds automation helpers.

Summary:
- Add central `Vault Conventions` page and link it from dashboard and project home.
- Shorten and deduplicate `Vault Workflow` and `Vault Usage Guide` references.
- Convert `Decisions.md` to a short summary and use `Decision Log` for chronology.
- Add `obsidian/agent_instructions.md` with agent preferences to reduce back-and-forth.
- Add `.github/PULL_REQUEST_TEMPLATE.md` and `.github/COMMIT_TEMPLATE.md`.
- Add test runner scripts `scripts/run_tests.sh` and `scripts/run_tests.ps1`.
- Add basic `.pre-commit-config.yaml`.

Verification:
- Run `scripts/run_tests.ps1` (Windows) or `scripts/run_tests.sh` (Unix) and ensure tests pass.
- Confirm no secrets were committed.
- Ensure `requirements.txt` is updated by contributors when adding packages.

Notes for reviewer:
- Changes are documentation and developer tooling only; no runtime code changes.
