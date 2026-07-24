# Decisions

## Prinzipien
- Konfiguration über Umgebungsvariablen und eine zentrale Konfigurationsdatei
- Keine Secrets im Quellcode
- In-Memory-Bildverarbeitung statt temporäre Dateiablage
- Unit-Tests und Mocks für externe Dienste
- Zentrales Logging statt Print-Ausgaben

## Wichtige Entscheidungen
### Dev-Notes als zentrale Wissensbasis
- Ein eigener Dev-Notes-Bereich dient als Projektgedächtnis.
- Der Obsidian-Vault wird diese Wissensbasis nun als aktives Werkzeug ergänzen.

### Teststrategie
- Die Flask-API wird über einen Test-Client simuliert.
- Externe Google-Services werden durch Mocks abgedeckt.

### Logging-Strategie
- Ein zentrales Logging-Modul soll die Ausgaben konsistent machen.
