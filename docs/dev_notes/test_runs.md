# Test Runs

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
