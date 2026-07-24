# Project Learnings

## Wichtige Erkenntnisse aus dem Projekt

### 1. Tests sind ein zentraler Qualitätsfaktor
- Die API wurde erfolgreich über einen Test-Client simuliert.
- Externe Dienste wie Google Calendar und Gmail sollten über Mocks abgesichert werden.
- Tests helfen dabei, die Logik unabhängig von sensiblen externen Abhängigkeiten zu prüfen.

### 2. Konfiguration sollte früh zentralisiert werden
- Secrets und Pfade sollten nicht im Code fest verdrahtet sein.
- Umgebungsvariablen und eine zentrale Konfigurationsdatei sind die bessere Lösung.

### 3. Bildverarbeitung sollte in-memory bleiben
- Temporäre Dateioperationen machen die Pipeline unnötig kompliziert.
- Eine RAM-basierte Verarbeitung ist robuster und einfacher zu testen.

### 4. Logging und Fehlerbehandlung sind nicht optional
- Ein zentrales Logging ist wichtig für Debugging und spätere Wartung.
- Klare Fehlerbehandlung verbessert sowohl Stabilität als auch Betriebssicherheit.

### 5. Der Vault ist nur dann nützlich, wenn er gepflegt wird
- Gute Dokumentation ist nur dann wertvoll, wenn sie regelmäßig aktualisiert wird.
- Struktur, Klarheit und regelmäßige Pflege sind wichtiger als große Dokumentmengen.
