# Architektur & aktueller Systemstand

## Komponenten

### `src/api_flask/room_monitor_server.py`
- Haupt-API-Server mit Flask
- Authentifizierung per Header-Token (`X-Device-Token`)
- Google-Integration für Kalender (`calendar.events().list`) und Gmail (`messages().send`)
- Endpunkte:
  - `/status` prüft, ob ein aktueller Termin aktiv ist
  - `/upload` nimmt ein Bild entgegen, analysiert es und sendet ggf. Mails
- Derzeitige Datenflussprobleme:
  - Bild wird in `VISION_BILD` als temporäre Datei geschrieben
  - Pfad- und Secret-Konfiguration sind teilweise hartkodiert
  - Es gibt zwei `token_ok()`-Funktionen, von denen nur die zweite verwendet wird
  - `credentials.json` und `token.json` werden direkt im Projekt erwartet

### `src/ki_zeugs/vision_mock.py`
- Bildanalyse per Ultralytics YOLO
- Lädt das Modell aus `src/ki_zeugs/yolov8n.pt`
- Derzeitige Eingabe: festes Bild `room.jpg` im gleichen Ordner
- Analysiert einen Bildpfad, statt bereits geladene Bilddaten zu verarbeiten
- Gibt `True` zurück, wenn Personen erkannt werden

## Verantwortlichkeiten

### API / Server
- `room_monitor_server.py` ist verantwortlich für:
  - HTTP-Schnittstellen und Endpunkte
  - Authentifizierung und Sicherheitsprüfung
  - Google-Kalenderabfrage und Mailversand
  - Koordination des Bildanalyseprozesses
  - Fehlerbehandlung auf der API-Ebene
  - Konfigurations- und Secret-Ladeprozesse

### Vision / Bildanalyse
- `vision_mock.py` ist verantwortlich für:
  - Laden und Verwenden des KI-Modells
  - Verarbeitung von Eingabebildern
  - Erkennung von Personen im Raum
  - Rückgabe eines einfachen Ergebnisses (`raum_besetzt` / `raum_frei`)

### Konfiguration / Secrets
- Aktuell ist die Verwaltung verantwortlich für:
  - Zugriff auf `credentials.json` und `token.json`
  - Laden von `DEVICE_TOKEN` und `OWN_EMAIL`
  - Festlegung von Modell- und Bildpfaden
- Diese Verantwortung sollte später in ein eigenes Modul (`config.py`) ausgelagert werden.

### Utilities / Infrastruktur
- Dinge wie:
  - Logging
  - Fehlerprotokollierung
  - Pfadmanagement
  - modulare Service-Schichten
  sollten in Zukunft in eigene Hilfs- oder Dienstmodule verschoben werden.

## Konfiguration und Secrets
- `DEVICE_TOKEN` ist direkt im Code hartkodiert
- `OWN_EMAIL` ist ebenfalls fest hinterlegt
- `credentials.json` und `token.json` werden aus dem Arbeitsverzeichnis geladen
- `.gitignore` enthält `credentials.json` und `token.json`, aber nicht unbedingt Pfade in `src/api_flask`
- Aktuelle Struktur unterstützt keine externe Konfigurationsdatei außerhalb des Projekts

## Technische Schulden

### Harte Pfade
- `os.path.join(SRC_DIR, "ki_zeugs", "room.jpg")` in `room_monitor_server.py`
- `BASE_DIR = os.path.dirname(__file__)` + `sys.path.insert(0, SRC_DIR)` im Server
- `room.jpg` und Modellpfad in `vision_mock.py`

### Geheimnisse im Code
- `DEVICE_TOKEN = "***REMOVED-DEVICE-TOKEN***"`
- `OWN_EMAIL = "removed-email@example.invalid"`
- `credentials.json` und `token.json` werden im Projekt gespeichert

### Doppelte / unsaubere Logik
- Zwei `token_ok()`-Definitionen in `room_monitor_server.py`
- `sys.path`-Manipulation zur Modulauflösung
- Bildverarbeitung über Datei statt in-memory Pipeline

### Fehlendes Logging & Fehlerhandling
- Nutzung von `print()` statt `logging`
- Fehlende zentrale Fehlerbehandlung
- Keine klare Trennung zwischen API-Logik und Service/Utility-Schichten

## Datenfluss aktuell
1. Request an `/upload` erhält binäre Bilddaten
2. Bild wird in `src/ki_zeugs/room.jpg` geschrieben
3. `check_raum_status()` analysiert das gespeicherte Bild
4. Temporäre Datei wird gelöscht
5. Bei leerem Raum und aktivem Termin werden Mails versendet

## Erste Verbesserungsansätze
- Bilddaten im RAM verarbeiten, statt temporär zu speichern
- Konfiguration und Secrets über Umgebungsvariablen oder externe Pfade laden
- Zentrale Start- und Konfigurationsprüfung einführen
- Logging anstelle von `print()` nutzen
- Dokumentation der Komponenten und Datenflüsse erweitern
