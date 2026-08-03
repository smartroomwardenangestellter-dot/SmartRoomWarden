# Architektur & aktueller Systemstand

Stand: 2026-08-03 (gegen `src/` verifiziert, vorheriger Stand war seit 2026-07-30 inkonsistent mit dem Code).

## Komponenten

### `src/api_flask/room_monitor_server.py`
- Haupt-API-Server mit Flask
- Authentifizierung per Header-Token (`X-Device-Token`)
- Google-Integration für Kalender (`calendar.events().list`) und Gmail (`messages().send`)
- Endpunkte:
  - `/status` prüft, ob ein aktueller Termin aktiv ist
  - `/upload` nimmt ein Bild entgegen, analysiert es und sendet ggf. Mails
  - `/health` einfacher Betriebscheck
- Genau eine `token_ok()`-Funktion (Zeile 156)
- Konfiguration und Secrets werden vollständig über `src/config.py` geladen, keine Hardcoded-Fallbacks (siehe `decisions.md` #7)

### `src/ki_zeugs/vision_mock.py`
- Bildanalyse per Ultralytics YOLO
- Lädt das Modell aus `src/ki_zeugs/yolov8n.pt` (`get_model()`), wird von der API gecacht statt bei jedem Upload neu geladen
- `check_raum_status(image_bytes: bytes, model=None)` verarbeitet bereits geladene Bilddaten (`cv2.imdecode`) - kein Datei-Umweg im Server-Pfad
- Das feste Bild `room.jpg` existiert nur noch als Fallback für den manuellen CLI-Testlauf (`python vision_mock.py`, `__main__`-Block), nicht im Produktionspfad
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
  - Verarbeitung von Eingabebildern (in-memory)
  - Erkennung von Personen im Raum
  - Rückgabe eines einfachen Ergebnisses (`raum_besetzt` / `raum_frei`)

### Konfiguration / Secrets
- `src/config.py` ist verantwortlich für:
  - Laden von `.env`/`.env.<mode>` (Runtime-Mode `simulation`/`system`)
  - Auflösen von `DEVICE_TOKEN`/`OWN_EMAIL` aus Umgebungsvariablen (kein Fallback)
  - Zugriff auf `credentials.json` und `token.json`
  - Festlegung von Modell- und Bildpfaden

### Utilities / Infrastruktur
- `src/logger.py`: zentrales Logging mit RotatingFileHandler (siehe `decisions.md` #4)
- Startup- und Konfigurationsprüfung vor dem eigentlichen Request-Handling

## Datenfluss aktuell
1. Request an `/upload` erhält binäre Bilddaten (`request.get_data()`)
2. `check_raum_status(image_bytes, model=...)` dekodiert die Bytes direkt im RAM (`np.frombuffer` + `cv2.imdecode`) - keine temporäre Datei
3. Bei erkannter Person: Antwort "Raum besetzt"
4. Bei leerem Raum und aktivem Termin, der seit ≥10 Minuten läuft: Mail an die Teilnehmer (außer den eigenen)

## Begriffe

Aus dem ehemaligen `obsidian/`-Glossar übernommen, hier ist der einzige Ort dafür:

- **Room Status**: Zustand eines Raums, z. B. besetzt oder leer
- **Active Calendar Event**: laufender Termin im Google Kalender
- **Upload Pipeline**: Verarbeitung eines eingehenden Bildes über die API
- **Ghost Meeting**: ein Termin, der als aktiv erkannt wird, obwohl kein echter Meeting-Status vorliegt (siehe Logging in `decisions.md`/`roadmap.md`)
- **Device Token**: Authentifizierungszeichen für den Zugriff auf den Server

## Bekannte technische Schulden (Stand 2026-08-03)

- `credentials.json` und `token.json` werden im Projektverzeichnis erwartet, nicht extern konfigurierbar
- Keine klare Trennung zwischen API-Logik und einer eigenen Service-/Utility-Schicht
- `docs/architektur.md` (diese Datei) beschreibt aktuell keine Refactoring-Vorschläge mehr, die bereits erledigt sind - siehe `roadmap.md` für offene Punkte

Bereits erledigt und daher hier nicht mehr als Schuld gelistet (verifiziert gegen den Code): Secrets im Code (behoben 2026-07-30, siehe `decisions.md` #7), doppelte `token_ok()`-Definition (nur noch eine), Bildverarbeitung über temporäre Datei (jetzt in-memory), fehlendes Logging (jetzt zentral über `logger.py`).
