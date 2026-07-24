# Sprintplan Woche 1–3

## Ziele
- Codebasis aufräumen und verstehen
- Bildverarbeitung in RAM umstellen
- Startup-, Konfigurations- und Fehlerhandling verbessern
- Logging einführen
- Erste Dokumentation und Struktur schaffen

---

## Woche 1: Analyse, Struktur und Dokumentation

### Fokus
- Codebasis verstehen
- Projektstruktur festlegen
- Technische Schulden identifizieren
- Erste Dokumentation erstellen

### Aufgaben
1. Codebasis auditieren
   - `src/api_flask/room_monitor_server.py` analysieren
   - `src/ki_zeugs/vision_mock.py` analysieren
   - vorhandene Pipeline, Konfiguration und Abhängigkeiten dokumentieren
2. Projektstruktur festlegen
   - klare Bereiche definieren: `api`, `vision`, `config`, `utils`
   - harte Pfade erkennen
   - aktuelle Secrets / Tokens identifizieren
3. Dokumentation anlegen
   - `docs/Vorgehen.md` überprüfen und ergänzen
   - neues Dokument `docs/architektur.md` oder `docs/current_state.md` starten
   - offene Punkte als Liste festhalten
4. Technische Schulden priorisieren
   - mögliche schnell lösbare Probleme markieren
   - größere Refaktor-Schritte einordnen

### Ergebnis
- Überblick über Architektur und Komponenten
- Liste offener Aufgaben und Schulden
- Klare Struktur für das weitere Refactoring

---

## Woche 2: Konfiguration, RAM-Verarbeitung und Startup

### Fokus
- Konfiguration und Secrets auslagern
- Upload/Analyse ohne Festplattenzugriff
- zentrale Start- und Konfigurationsprüfung einführen

### Aufgaben
1. Konfigurations-Setup
   - `GOOGLE_CREDENTIALS_PATH`, `GOOGLE_TOKEN_PATH`, `SMARTROOMWARDEN_DEVICE_TOKEN` definieren
   - `config.py` oder ähnliches für zentrales Laden einführen
   - `.gitignore` prüfen und sensible Pfade ergänzen
2. RAM-basierte Bildverarbeitung
   - `upload()` so umbauen, dass Bilddaten als `bytes` verarbeitet werden
   - `vision_mock` / Bildanalyse so anpassen, dass sie `ndarray` akzeptiert
   - temporäre Speicherung von `room.jpg` entfernen
3. Startup- und Fehlerprüfung
   - zentralen Entry-Point in `src/api_flask` definieren
   - beim Start vorhandene Konfiguration prüfen
   - fehlende Ressourcen und falsche Pfade früh melden
4. Tests und Validation
   - einfacher Funktionscheck der Upload-Pipeline
   - sicherstellen, dass das System mit lokalem Modell startet

### Ergebnis
- sichere Konfigurationsbasis
- Bildverarbeitung ohne temporäre Dateien
- stabilerer Startprozess

---

## Woche 3: Logging, Fehlerhandling und erste Stabilisierung

### Fokus
- Logging-Architektur einführen
- zentrale Fehlerbehandlung definieren
- Stabilität und Nachvollziehbarkeit erhöhen

### Aufgaben
1. Logging einführen
   - zentrale `logging`-Konfiguration erstellen
   - rotierende Logdateien / zentraler Logpfad definieren
   - Events wie Startup, Analyse, Mailversand, Fehler loggen
2. Fehlerbehandlung verbessern
   - `Flask`-Errorhandler einrichten
   - aussagekräftige Fehlermeldungen und Statuscodes definieren
   - Exceptions sauber unterscheiden (Konfiguration, Auth, Vision, API)
3. Stabilität testen
   - Fehlerfälle durchspielen: fehlende Auth, ungültige Bilder, Kalenderfehler
   - Logausgabe prüfen
4. Dokumentation ergänzen
   - `docs/Vorgehen.md` um Woche 1–3 Ergebnisse aktualisieren
   - `docs/operations.md` als erster Betriebskurzbogen beginnen

### Ergebnis
- zentrales Logging und Fehlerhandling
- stabilere Anwendung im laufenden Betrieb
- dokumentierter Status nach drei Wochen

---

## Ergänzende Hinweise
- Wenn Zeit bleibt, kann am Ende von Woche 3 ein einfacher Dashboard-Prototyp als Proof of Concept angelegt werden.
- Hardware-Optimierungen, Wartungskonzept und ESP-Flashing-Tool sollten in einem zweiten Sprintblock folgen.
- Priorisiere zuerst Stabilität, Sicherheit und saubere Trennung der Komponenten.
