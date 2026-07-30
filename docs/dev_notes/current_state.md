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
- Die Konfigurationslogik lädt `.env.system` jetzt zuverlässig, wenn der Server im System-Modus gestartet wird
- Die Google-Credentials-Pfade werden jetzt korrekt aus den Projektdateien aufgelöst
- 2026-07-30: Hardcoded Secrets entfernt (siehe Sicherheit unten)

### Sicherheit (Stand 2026-07-30)
- `esp32/esp32_cam.ino`: WLAN-SSID/Passwort und Device-Token sind nicht mehr im Quellcode - liegen jetzt in `esp32/secrets.h` (gitignored, Template: `esp32/secrets.h.example`)
- `src/config.py`: `DEVICE_TOKEN`/`OWN_EMAIL` haben keinen Hardcoded-Fallback mehr - fehlt die Env-Var, schlägt `validate_configuration()`/`get_services()` laut fehl statt den bekannten Token stillschweigend zu nutzen
- `client.setInsecure()` in `esp32_cam.ino` bleibt bestehen, ist jetzt aber im Code als bewusst akzeptiertes Risiko dokumentiert: der Pi startet Flask mit `ssl_context="adhoc"`, das bei jedem Neustart ein neues Self-signed-Zertifikat erzeugt - Cert-Pinning ist damit ohne Server-Umbau auf ein persistentes Zertifikat nicht sinnvoll möglich
- **Offen (nicht code-seitig lösbar):** Das Repo ist öffentlich auf GitHub - das reale WLAN-Passwort und der alte Device-Token stehen weiterhin in der Git-History (Commit `4d4a6f1`). WLAN-Passwort-Rotation am Router, Device-Token-Rotation + Re-Flash des ESP32, und ggf. Git-History-Bereinigung sind offene manuelle Schritte

### Offene Aufgaben
- reale Google-/Mail-Integration auf dem Zielserver verifizieren
- Betriebs- und Runbook-Dokumentation weiter ausbauen
- Deployment- und Reverse-Proxy-Konfiguration für Debian 13 vorbereiten
- WLAN-Passwort rotieren, Device-Token rotieren + ESP32 neu flashen, Git-History-Bereinigung entscheiden (siehe Sicherheit oben)
