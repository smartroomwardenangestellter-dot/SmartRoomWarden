# SmartRoomWarden Agent Instructions

## Purpose
This repository is the working codebase and technical documentation for SmartRoomWarden. The agent should support productive, safe, and traceable development.

## Core working rules
- Keep repository documentation in `docs/` (incl. `docs/dev_notes/`) as the single source of technical project documentation - there is no separate in-repo knowledge base.
- When important decisions, findings, or root-cause fixes are made, record them in `docs/dev_notes/decisions.md` and `docs/dev_notes/current_state.md`.
- Prefer small, verifiable changes over broad refactors.
- Do not commit secrets, credentials, tokens, or local environment files.

## Required workflow
1. Understand the current task and the relevant repository context.
2. Make the smallest root-cause fix that matches the task.
3. Add or update a regression test when changing behavior.
4. Verify with the relevant test command before claiming success.
5. Record important decisions and current-state changes in `docs/dev_notes/`.

## Dependency rule
- If new Python packages are introduced, update `requirements.txt` as part of the change.
- Do not add dependencies without documenting the reason.

## Repository conventions
- Use the existing Python test suite and prefer `unittest`-based verification.
- Keep configuration centralized in `src/config.py`.
- Keep logging centralized in `src/logger.py`.
- Prefer in-memory image handling for the upload pipeline.
- Avoid hardcoded secrets, paths, or local-only environment assumptions in source files.

## Documentation expectations
- Use `docs/` for all stable technical context, current status, and decision history.
- The project owner separately maintains a personal second-brain vault outside this repository for cross-project knowledge, process learnings, and working-session logs - repo-scoped agents do not have access to it and should not assume it exists as a write target.

## Default-agent routing rules
- Analyze the user's request first and decide whether a specialized agent is needed.
- If the request is primarily about repository execution, safe changes, or docs alignment, route it to the `repo-ops-agent`.
- If the request is primarily about validation, reproduction, failing tests, or evidence-based verification, route it to the `quality-verification-agent`.
- If the task is general, mixed, or ambiguous, stay with the default agent and keep the work small, verifiable, and well documented in `docs/`.

## Routing decision matrix
- Code change / bug fix / docs alignment / repo hygiene / small engineering task -> `repo-ops-agent`
- Test run / reproduction / proof / diagnosis / verification -> `quality-verification-agent`
- If both are involved, pick the dominant intent and delegate that specialty first; keep the default agent in charge of the overall workflow.
- Do not route every request to a specialized agent just because one exists. Only delegate when it improves clarity, safety, or traceability.

## Safety guardrails
- Never commit credentials, `.env` files, access tokens, keys, or local secrets.
- Always verify that the repository remains testable after edits.
- If a task turns into a larger refactor, split it into small, reviewable steps.
- Do not add new dependencies without documenting the reason and updating `requirements.txt` if needed.
- Keep `docs/` internally consistent - verify claims against actual source before writing them down.
