# Test Runs

## 2026-08-03: Security-/CI-Nachzügler aus PR #7 gemergt

- 4 neue Tests in `tests/test_room_monitor_server.py` (Herkunft: Cherry-Pick aus dem nie gemergten `claude/onboarding`-Branch, siehe `decisions.md` #9):
  - `test_status_unauthorized_with_wrong_token`
  - `test_status_unauthorized_when_device_token_not_configured`
  - `test_upload_rejects_oversized_payload`
  - `test_upload_rejects_non_image_content_type`
- Gesamtzahl Tests jetzt **24** (`test_room_monitor_server.py`: 19, `test_config.py`: 3, `test_vision_mock.py`: 2 - per `grep -rc "    def test_" tests/*.py` gezählt)
- **Nicht live ausgeführt in der Konsolidierungs-Sandbox** (kein `flask`, kein `cv2`, kein `pip` verfügbar) - stattdessen die 4 neuen Testfälle manuell gegen die Implementierung geprüft (Assertions passen zur `token_ok()`/`MAX_UPLOAD_BYTES`/Content-Type-Logik). Live-Verifikation mit echtem `flask`/`cv2` steht noch aus (offener Punkt aus PR #7s eigenem Test-Plan)
- Ab diesem Merge läuft die Suite zusätzlich automatisch bei jedem Push/PR auf `main` über GitHub Actions (`.github/workflows/tests.yml`)

## 2026-07-30: Regressionscheck nach Secrets-Fix

- Testdatei: gesamte Suite (`test_config.py`, `test_room_monitor_server.py`, `test_vision_mock.py`)
- Ausführung: `python3 -m unittest discover -s tests`
- Baseline (vor der Änderung, per `git stash`): 4 Failures, 1 Error
- Nach Entfernen der Hardcoded-Fallbacks in `config.py`: zunächst 12 Failures, 1 Error - Ursache: `test_room_monitor_server.py` cachte `DEVICE_TOKEN`/`OWN_EMAIL` beim Modul-Import und verließ sich implizit auf den alten Hardcoded-Default
- Fix: `test_room_monitor_server.py` setzt jetzt vor dem Modul-Import explizit `SMARTROOMWARDEN_DEVICE_TOKEN`/`SMARTROOMWARDEN_OWN_EMAIL` (`os.environ.setdefault(...)`)
- Ergebnis danach: wieder 4 Failures, 1 Error - identisch zur Baseline, keine Regression durch den Secrets-Fix. Die verbleibenden 4+1 sind vorbestehende, unabhängige Bugs (`test_vision_mock`, `test_config.test_dotenv_values_are_loaded`, zwei `test_upload_*`-Fälle) - nicht Teil dieser Änderung

## 2026-07-27: Server-Härtung und Health-Check

- Testdatei: `tests/test_room_monitor_server.py`
- Ausführung: `python -m unittest discover -s tests -p 'test_*.py'`
- Ergebnis: `OK`
- Anzahl Tests: 19

## 2026-07-27: Live-Server-Test mit echter HTTP-Simulation

- Umgebung: lokale Projekt-Umgebung `.venv`
- Ausführung: `python -m unittest discover -s tests -p 'test_config.py'` und `python -m unittest discover -s tests -p 'test_*.py'`
- Ergebnis: `OK`, 20 Tests
- Live-HTTP-Checks:
  - `GET /health` → `200 {"status":"ok"}`
  - `POST /upload` mit Dummy-Body und Token → `200 Kein aktiver Termin`
- Erkenntnisse:
  - Die Konfiguration wird jetzt zuverlässig aus `.env.system` geladen, wenn kein expliziter Runtime-Modus gesetzt ist.
  - Die Google-Credentials-Pfade werden korrekt auf `./credentials/credentials.json` und `./credentials/token.json` aufgelöst.
  - Der Device-Token muss exakt mit dem ESP- und Client-Code übereinstimmen, sonst wird der Zugriff abgelehnt.

### Abgedeckte Szenarien
- `/status` ohne Token → 401 unauthorized
- `/status` mit aktiver Terminantwort → 200 true
- `/status` ohne Termin → 200 false
- `/upload` ohne Bilddaten → 400 Kein Bild
- `/upload` mit leerem Raum und mindestens 10 Minuten laufendem Termin → E-Mail-Versand-Simulation
- `/upload` mit Person im Raum → 200 Raum besetzt
- `/upload` ohne aktiven Termin → 200 Kein aktiver Termin
- `/health` mit gültiger Konfiguration → 200 ok
- Server-Config-Overrides über Umgebungsvariablen

### Erkenntnisse
- Die API-Tests sind weiterhin stabil und decken die wichtigsten Routen und Fehlerfälle ab
- Der neue Health-Endpoint ist sauber abgesichert
- Die Server-Konfiguration ist für Deploy-Zwecke flexibel einstellbar

## 2026-07-23 bis 2026-07-24: Frühere Prototyp-Verifikation

- Ausführung: `python -m unittest discover -s tests -p 'test_*.py'`
- Umgebung: Projekt-Interpreter der lokalen virtuellen Umgebung `.venv`
- Ergebnis: Prototyp-Tests erfolgreich

### Erkenntnisse
- Der Prototyp war zunächst auf einfache Flask- und Upload-Scenario beschränkt
- Die Dokumentation musste auf den späteren Server-Härtungsstand erweitert werden
