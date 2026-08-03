@AGENTS.md

## Claude Code-specific instructions
- Full technical documentation lives in `docs/` (start at `docs/dev_notes/README.md`) - read `docs/architektur.md` and `docs/dev_notes/current_state.md` before making changes.
- Run the test suite before claiming any change works: `python -m unittest discover -s tests -p 'test_*.py'` (or `scripts/run_tests.sh` / `scripts/run_tests.ps1`).
- This file exists only so Claude Code auto-loads `AGENTS.md` at session start (Claude Code reads `CLAUDE.md`, not `AGENTS.md`, automatically) - keep `AGENTS.md` as the single source of agent conventions, don't duplicate its content here.
