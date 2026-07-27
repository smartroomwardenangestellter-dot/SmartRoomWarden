# Quick Links

## Wichtige Pfade
- Projekt-Root: `c:\Users\MLampe\OneDrive - COMPUTACENTER\Dokumente\GitHub\SmartRoomWarden`
- Haupt-Server: `src/api_flask/room_monitor_server.py`
- Vision-Modul: `src/ki_zeugs/vision_mock.py`
- Konfiguration: `src/config.py`
- Logging: `src/logger.py`
- Logs-Verzeichnis: `logs/`
- Tests: `tests/test_room_monitor_server.py`
- Dev Notes: `docs/dev_notes/`
- Betriebs-Runbook: `docs/dev_notes/operations.md`
- Beispiel-Konfigurationen: `config_templates/`

## Wichtige Umgebungsvariablen
- `SMARTROOMWARDEN_DEVICE_TOKEN`
- `SMARTROOMWARDEN_OWN_EMAIL`
- `GOOGLE_CREDENTIALS_PATH`
- `GOOGLE_TOKEN_PATH`
- `SMARTROOMWARDEN_HOST`
- `SMARTROOMWARDEN_PORT`
- `SMARTROOMWARDEN_SSL`

## Nützliche Kommandos
- Tests ausführen: `python -m unittest discover -s tests -p 'test_*.py'`
- Server starten: `python src/api_flask/room_monitor_server.py`
- Health-Check: `curl http://127.0.0.1:5000/health`
- Requirements installieren: `python -m pip install -r requirements.txt`

## Checkpoints
- Aktueller Teststatus: `docs/dev_notes/test_runs.md`
- Aktueller Projektstand: `docs/dev_notes/current_state.md`
- Entscheidungen: `docs/dev_notes/decisions.md`
