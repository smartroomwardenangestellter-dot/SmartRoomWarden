# Aktueller Projektstatus

## Komponenten

### API-Server
- `src/api_flask/room_monitor_server.py`
- Flask-Anwendung mit den Endpunkten `/status`, `/upload` und `/health`
- Prüft Google-Kalendertermine und versendet Gmail-Benachrichtigungen
- Verarbeitet Bilddaten direkt aus dem Request-Body im RAM

### Bildanalyse
- `src/ki_zeugs/vision_mock.py`
- YOLO-basierte Personenerkennung über Ultralytics
- Verarbeitet Bildbytes und gibt `True` zurück, falls Personen erkannt werden

### Konfiguration
- `src/config.py`
- `src/logger.py`
- Umgebungskonfiguration für Google-Credentials, Device-Token und Server-Parameter

## Aktueller Zustand

### Stabilität
- Der Prototyp ist lokal mit Tests verifiziert
- Die API-Endpunkte sind mit einem Flask-Test-Client abgesichert
- Die neue Health-Route `/health` ist verfügbar und dient als einfacher Betriebscheck
- Google-Credentials und Token bleiben lokal und werden nicht ins Repository verteilt

### Tests
- `tests/test_room_monitor_server.py` deckt API-Aufrufe und Fehlerszenarien ab
- Die aktuelle Regressionstest-Suite läuft erfolgreich mit 19 Tests

### Aktuelle Verbesserungen
- Health-Endpoint für einfache Systemprüfungen ergänzt
- YOLO-Modell wird gecacht, statt bei jedem Upload neu zu laden
- Konfigurationsprüfung und Server-Start sind deployfreundlicher gestaltet
- Import-Fallbacks sorgen dafür, dass der Server bei fehlenden optionalen Paketen nicht sofort abstürzt

### Offene Aufgaben
- reale Google-/Mail-Integration auf dem Zielserver verifizieren
- Betriebs- und Runbook-Dokumentation weiter ausbauen
- Deployment- und Reverse-Proxy-Konfiguration für Debian 13 vorbereiten
