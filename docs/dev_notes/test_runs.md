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

## 2026-07-24: Wiederholte Verifikation des Prototyp-Status

- Ausführung: `python -m unittest discover -s tests -p 'test_*.py'`
- Umgebung: Projekt-Interpreter der lokalen virtuellen Umgebung `.venv`
- Ergebnis: `Ran 12 tests in 0.220s` und `OK`

### Abgedeckte Szenarien
- Status-Endpunkt mit fehlender Konfiguration
- Status-Abfrage mit aktivem und ohne aktiven Termin
- Upload ohne Bilddaten
- Upload mit Personen im Raum
- Upload mit leerem Raum und laufendem Termin
- Bildanalyse-Fehlerfälle, inklusive ungültiger Bildbytes

### Erkenntnisse
- Die lokale Projekt-Umgebung ist jetzt zur Verifikation des Prototyps geeignet
- Die Kernlogik ist in den aktuellen Tests stabil abgesichert
- Die Dokumentation muss den verifizierten Prototype-Status sauber im Dev-Notes-Bereich widerspiegeln
