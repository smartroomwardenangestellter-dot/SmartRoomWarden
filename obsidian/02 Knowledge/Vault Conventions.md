# Vault Conventions

Diese Checkliste fasst verbindliche Konventionen für das Projekt zusammen — kurz und handlungsorientiert.

- Wenn neue Python-Pakete hinzugefügt werden: immer `requirements.txt` aktualisieren (pinnen nach Bedarf).
- Keine Secrets in Repo oder Vault (Credentials, Tokens, private .env). Sensible Daten bleiben extern.
- Dateinamen ohne Sonderzeichen; Pfade sollen shell-safe sein (keine `&`, `%`, ` ` etc.).
- Tests müssen lokal laufen (`python -m unittest`) bevor in `main` gemerged wird.
- Dokumentation pflegen: Änderungen an Code oder Struktur erfordern relevante Doc-Links/Updates im Vault.
- Wichtige Entscheidungen: kurze Zusammenfassung in `Decisions.md` + Eintrag in `Decision Log` (chronologisch).
- Verwende Templates aus `03 Templates/` für konsistente Notizen (Decision, Review, Daily Note).
- Archivieren statt löschen: abgeschlossene Themen in `04 Archive/` verschieben.

Pflegehinweis:
- Mindestens einmal pro Sprint/Woche sollte jemand den Vault auf veraltete oder doppelte Einträge prüfen.

