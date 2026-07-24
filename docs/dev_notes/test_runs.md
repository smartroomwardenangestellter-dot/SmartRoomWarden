# Test Runs

## 2026-07-23: Flask API Simulation

- Testdatei: `tests/test_room_monitor_server.py`
- Ausführung: `python -m unittest discover -s tests -p 'test_*.py'`
- Ergebnis: `OK`
- Anzahl Tests: 7

### Abgedeckte Szenarien
- `/status` ohne Token → 401 unauthorized
- `/status` mit aktiver Terminantwort → 200 true
- `/status` ohne Termin → 200 false
- `/upload` ohne Bilddaten → 400 Kein Bild
- `/upload` mit leerem Raum und mindestens 10 Minuten laufendem Termin → E-Mail-Versand-Simulation
- `/upload` mit Person im Raum → 200 Raum besetzt
- `/upload` ohne aktiven Termin → 200 Kein aktiver Termin

### Erkenntnisse
- Mocks für Google-Services und Bildanalyse funktionieren zuverlässig
- Test-Client-Setup ist geeignet für weitere API-Simulationen
- `room_monitor_server.py` kann weiterhin verbessert werden, um extern konfigurierte Google-Credentials abzudecken

## 2026-07-24: ImportError bei Tests

- Fehler: `ModuleNotFoundError: No module named 'certifi'`
- Ursache: Die lokale Python-Umgebung des Projekts hatte die Abhängigkeit `certifi` nicht installiert.
- Lösung: `certifi` im Projekt-Environment installieren.
- Verifikation: Der Testlauf wurde danach erneut ausgeführt und der Import-Fehler war behoben.
