# Aktueller Projektstatus

## Komponenten

### API-Server
- `src/api&flask/room_monitor_server.py`
- Flask-Anwendung mit den Endpunkten `/status` und `/upload`
- Prüft Google-Kalendertermine und versendet Gmail-Benachrichtigungen
- Nutzt `request.get_data()` für Bilddaten

### Bildanalyse
- `src/ki_zeugs/vision_mock.py`
- YOLO-basierte Personenerkennung
- Verarbeitet eingehende Bildbytes und gibt `True` zurück, falls Personen erkannt werden

### Konfiguration
- `src/config.py`
- `src/logger.py`
- Umgebungskonfiguration für Google-Credentials und Device-Token

## Aktueller Zustand

### Stabilität
- Der erste funktionale Prototyp ist auf `main` verifiziert
- API-Endpunkte funktionieren mit Test-Client-Simulation
- Google-Credentials fehlen in der lokalen Testumgebung, daher werden Google-Services nicht produktiv getestet
- Die Betriebsdokumentation wird im aktuellen Branch `feature/ops-runbook` als Runbook-Prototyp weitergeführt

### Tests
- `tests/test_room_monitor_server.py` simuliert API-Aufrufe und mocks die Service-Aufrufe
- Die aktuelle Regressionstest-Suite läuft erfolgreich mit 12 Tests

### Probleme
- `room_monitor_server.py` verwendet derzeit noch direkte `sys.path`-Manipulation
- `vision_mock.py` lädt das Modell beim Import, was Startup-Zeit kostet
- `credentials.json` und `token.json` sind noch nicht extern konfiguriert
- Fehlertoleranz bei Google-API-Fehlern muss verbessert werden

## Offene Aufgaben
- `docs/dev_notes/test_runs.md` regelmäßig pflegen
- `docs/dev_notes/decisions.md` mit Architekturentscheidungen füllen
- `docs/dev_notes/quick_links.md` mit wichtigen Pfaden/Umgebungsvariablen ergänzen
- `docs/dev_notes/operations.md` als erste Betriebs- und Runbook-Basis weiter ausbauen
- `.gitignore` auf weitere sensible Dateien prüfen
