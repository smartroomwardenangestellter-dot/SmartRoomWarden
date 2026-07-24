# TODOs und Issues

## Übersicht
Diese Datei enthält die abgeleiteten Aufgaben und Issues aus dem Sprintplan für die nächsten Wochen.

---

## Woche 1: Analyse, Struktur und Dokumentation

### TODOs
- [ ] Audit der aktuellen Codebasis durchführen
  - `src/api&flask/room_monitor_server.py` analysieren
  - `src/ki_zeugs/vision_mock.py` analysieren
- [ ] Verantwortlichkeiten der Module dokumentieren
  - API / HTTP / Google-Integration
  - Bildanalyse / KI
  - Konfiguration / Secrets
- [ ] Technische Schulden identifizieren und priorisieren
  - harte Pfade
  - harte Tokens / Secrets im Code
  - doppelte Funktionen
  - fehlendes Logging
- [ ] Dokumentation erstellen oder ergänzen
  - `docs/Vorgehen.md` überprüfen
  - `docs/architektur.md` oder `docs/current_state.md` anlegen
- [ ] Liste offener Probleme und Verbesserungen erstellen

### Issues
- `Issue: Projektarchitektur dokumentieren`
  - Beschreibe aktuelle Komponenten und Datenflüsse
- `Issue: Technische Schulden aufnehmen`
  - Liste aller bekannten Schwachstellen und Refactoring-Punkte
- `Issue: Projektstruktur reinigen`
  - Vorschlag für saubere Modulaufteilung erstellen

---

## Woche 2: Konfiguration, RAM-Verarbeitung und Startup

### TODOs
- [x] Zentrale Konfiguration implementieren
  - `config.py` anlegen
  - Umgebungsvariablen einführen: `GOOGLE_CREDENTIALS_PATH`, `GOOGLE_TOKEN_PATH`, `SMARTROOMWARDEN_DEVICE_TOKEN`
- [x] Sensitive Daten aus dem Code entfernen
  - harte Pfade ersetzen
  - Secrets nicht mehr direkt im `room_monitor_server.py` speichern
- [ ] `.gitignore` prüfen und sensible Dateien ergänzen
- [x] Upload-Endpoint so umbauen, dass Bilder im RAM verarbeitet werden
  - `request.get_data()` nutzen
  - `cv2.imdecode()` verwenden
- [x] Vision-Modul anpassen, damit es `bytes` oder `ndarray` entgegennimmt
- [x] Temporäre Dateioperationen aus der Bildpipeline entfernen
- [x] Startup- und Konfigurationsprüfung einführen
  - zentrale Prüfung auf notwendige Ressourcen
  - Fehlermeldungen bei fehlenden Konfigurationen

### Issues
- `Issue: Secrets auslagern`
  - Konfiguration und Tokens aus dem Code entfernen
- `Issue: RAM-Verarbeitung einführen`
  - Bildverarbeitung ohne Festplattenzugriff implementieren
- `Issue: Startprüfung einführen`
  - Vor dem Launch die Konfiguration und Ressourcen prüfen

---

## Woche 3: Logging, Fehlerhandling und Stabilisierung

### TODOs
- [ ] Zentrales Logging einrichten
  - Python `logging` konfigurieren
  - Rotating File Handler einrichten
  - Logverzeichnis (`logs/`) anlegen
- [ ] Ereignisse loggen
  - Systemstart
  - Konfigurationsprüfung
  - Uploads und Bildanalysen
  - erkannte Ghost Meetings
  - versendete Benachrichtigungen
- [ ] Fehlerbehandlung verbessern
  - Flask-Errorhandler einrichten
  - zentrale Ausnahme-Logik definieren
  - klare HTTP-Statuscodes und Fehlermeldungen
- [ ] Stabilität testen
  - Fehlerfälle prüfen: fehlende Auth, ungültige Bilder, Kalenderfehler
  - Logausgabe evaluieren
- [ ] Dokumentation aktualisieren
  - Ergebnisse in `docs/Vorgehen.md` einarbeiten
  - `docs/operations.md` als Betriebs- und Wartungsübersicht beginnen

### Issues
- `Issue: Logging-Konzept umsetzen`
  - Zentrales Logging und strukturierte Logausgabe definieren
- `Issue: Fehlerbehandlung zentralisieren`
  - Konsistente Fehlerreaktionen und saubere Diagnosen ermöglichen
- `Issue: Stabilitätscheck durchführen`
  - Fehlerfälle durchtesten und dokumentieren

---

## Ergänzende Themen

### TODOs
- [ ] Dashboard-Prototyp planen (optional)
- [ ] Betriebsdokumentation und Wartungskonzept starten
- [ ] Informationsflyer/Inhaltsplan erstellen
- [ ] ESP-Flashing-Tool konzipieren

### Issues
- `Issue: Dashboard-Anforderungen definieren`
  - Funktionen und UI-Bedarf für eine erste Version klären
- `Issue: Wartungskonzept erstellen`
  - Betriebsprozesse und Backup-Strategie dokumentieren
- `Issue: ESP-Flashing-Tool planen`
  - Einrichtung neuer Geräte und Firmware-Rollout strukturieren
