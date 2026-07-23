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
