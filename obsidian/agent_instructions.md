# Agent Instructions — Project Preferences

Zweck: zentrale Vorgaben für automatisierte Agenten und Contributors, um Rückfragen zu minimieren und konsistente Änderungen zu ermöglichen.

Standardannahmen
- Default branch: `main` (Branches für Änderungen: `feature/*`, `fix/*`, `chore/*`).
- Projekt-Interpreter: `.venv\Scripts\python.exe` (Windows) oder `.venv/bin/python` (Unix).
- Test-Befehl: `scripts/run_tests.ps1` (Windows) oder `scripts/run_tests.sh` (Unix).

Konventionen, die Agenten befolgen sollen
- Bevor Änderungen vorgeschlagen werden: sicherstellen, dass `python -m unittest discover -s tests -v` lokal läuft.
- Wenn neue Python-Abhängigkeiten hinzugefügt werden: `requirements.txt` aktualisieren und in der PR‑Checkliste erwähnen.
- Keine Secrets in Repo oder Vault committen. Leite Benutzer an, Umgebungsvariablen oder sichere Stores zu verwenden.
- Dateinamen sollen shell-safe sein (keine `&`, `?`, `%`, Leerzeichen).

Formatting & Commits
- Commit‑Konvention: `<type>(<scope>): short description` (z. B. `chore(vault): add conventions`).
- PRs sollten die `PULL_REQUEST_TEMPLATE.md` nutzen; die PR‑Beschreibung soll einen Verifikationsabschnitt enthalten.

Verifikation
- Nach Änderungen führt der Agent die Test-Skripte aus und meldet nur die relevanten Fehlermeldungen (nicht komplette Logs).

Agent‑Memory
- Agenten dürfen die folgenden Präferenzen speichern unter `/memories/repo/agent_prefs.md`:
  - Test-Befehl
  - Default branch
  - Commit-Message-Style

Fallbacks
- Wenn ein vorgeschlagener Patch unklar ist, frage maximal 2 kurze Rückfragen, keine freien Textdiskussionen.
