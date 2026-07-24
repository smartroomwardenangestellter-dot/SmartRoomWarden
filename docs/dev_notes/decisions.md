# Architektur- und Designentscheidungen

## Prinzipien
- Konfiguration über Umgebungsvariablen und zentrale `config.py`
- Keine Secrets im Quellcode
- In-Memory-Bildverarbeitung statt temporäre Dateiablage
- Unit-Tests und Mocking für externe Dienste (Google Calendar/Gmail)
- Zentrales Logging statt `print()`

## Getroffene Entscheidungen

### 1. Dev-Notes Ordner
- Ein eigener Ordner `docs/dev_notes/` dient als zentrale Entwickler-Wissensbasis
- Er enthält aktuelle Projektzustände, Testläufe und Entscheidungen

### 2. Teststrategie
- Flask-API wird über einen Test-Client simuliert
- Externe Google-Services werden durch `Mock`-Objekte abgedeckt
- Bildanalyse wird ebenfalls gemockt, um den Endpunkt isoliert zu prüfen

### 3. Konfigurationsstrategie
- `config.py` legt Pfade, Token und E-Mail-Adressen fest
- Nutzung von Umgebungsvariablen wie `SMARTROOMWARDEN_DEVICE_TOKEN`
- Abstraktion der Konfiguration vom Server-Code

### 4. Logging-Strategie
- Zentrales `logger.py` mit RotatingFileHandler
- Log-Ausgaben sollen sowohl Konsole als auch Logdateien bedienen
- Die Log-Struktur ermöglicht spätere Analyse und Debugging

### 5. Branch- und Release-Strategie für den Prototyp
- `main` bleibt der verifizierte Prototype-Release-Stand
- neue, klar abgegrenzte Roadmap-Phasen werden auf separaten Branches umgesetzt
- der Branch `feature/ops-runbook` dient der Betriebs- und Runbook-Phase ohne das Produktverhalten zu verändern

### 6. Betriebsdokumentationsstrategie
- die Dev-Notes werden als stabile Projekt-Dokumentation gepflegt
- ein Runbook-Prototyp in `docs/dev_notes/operations.md` dokumentiert erste Betriebs-Checks, Fehlerfälle und Recovery-Schritte
- Teammitglieder sollen damit den aktuellen Betriebszustand ohne Code-Risiko nachvollziehen können
