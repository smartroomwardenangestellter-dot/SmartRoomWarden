# SmartRoomWarden Agent Instructions

## Purpose
This repository is the project knowledge base and working codebase for SmartRoomWarden. The agent should support productive, safe, and traceable development.

## Core working rules
- Keep the Obsidian vault as the active working knowledge space.
- Keep repository documentation in `docs/dev_notes/` as stable project documentation.
- When important decisions, findings, or process lessons are discovered, capture them in the vault immediately.
- Prefer small, verifiable changes over broad refactors.
- Do not commit secrets, credentials, tokens, or local environment files.

## Required workflow
1. Understand the current task and the relevant repository context.
2. Make the smallest root-cause fix that matches the task.
3. Add or update a regression test when changing behavior.
4. Verify with the relevant test command before claiming success.
5. Record important learnings in the vault and keep the project docs aligned.

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
- Use the repository docs for stable technical context.
- Use the vault for active project memory, decisions, working notes, and next actions.
- When it changes the course of engineering, document the rationale in the vault.

## Default-agent routing rules
- Analyze the user's request first and decide whether a specialized agent is needed.
- If the request is primarily about vault maintenance, active knowledge capture, decisions, or project memory, route it to the `obsidian-vault-agent`.
- If the request is primarily about repository execution, safe changes, docs alignment, or minimal engineering work, route it to the `repo-ops-agent`.
- If the request is primarily about validation, reproduction, failing tests, or evidence-based verification, route it to the `quality-verification-agent`.
- If the task is general, mixed, or ambiguous, stay with the default agent and keep the work small, verifiable, and well documented in the vault.

## Routing decision matrix
- Vault / memory / notes / learnings / decisions / active project context -> `obsidian-vault-agent`
- Code change / bug fix / docs alignment / repo hygiene / small engineering task -> `repo-ops-agent`
- Test run / reproduction / proof / diagnosis / verification -> `quality-verification-agent`
- If two of the above are involved, pick the dominant intent and delegate that specialty first; keep the default agent in charge of the overall workflow.
- Do not route every request to a specialized agent just because one exists. Only delegate when it improves clarity, safety, or traceability.

## Safety guardrails
- Never commit credentials, `.env` files, access tokens, keys, or local secrets.
- Always verify that the repository remains testable after edits.
- If a task turns into a larger refactor, split it into small, reviewable steps.
- Do not add new dependencies without documenting the reason and updating `requirements.txt` if needed.
- Always preserve the division between the active vault and stable repository docs.
