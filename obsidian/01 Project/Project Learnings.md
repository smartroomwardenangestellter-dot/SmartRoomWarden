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

### 6. Konfigurations- und Fehlerpfade sollten früh abgesichert werden
- `.env`-Werte sollten aus dem Projektstamm geladen werden, damit das System auch in lokalen und testbaren Umgebungen zuverlässig läuft.
- Einfache, vorhersehbare Fehlerantworten für externe Dienste sind für Betrieb und Debugging wichtiger als rohe Exceptions.
- Der Status-Endpunkt sollte nicht direkt an Google- oder Dienstfehlern scheitern, sondern kontrolliert reagieren.

### 7. Typ- und Editor-Hinweise sind Teil der Qualitätssicherung
- Statische Analysefehler sollten nicht ignoriert werden, wenn sie die Lesbarkeit oder Wartbarkeit beeinträchtigen.
- Besonders bei Tests und dynamisch geladenen Modulen lohnt sich ein kleiner Abstraktions- oder Guard-Schritt, um die Typprüfung sauber zu halten.

### 8. Vision-Logik sollte modellseitig abstrahiert werden
- Der Bildanalyse-Code sollte nicht direkt an ein globales Modell gebunden sein, sondern über eine kleine Helper-Funktion konfigurierbar sein.
- Das macht Tests deutlich einfacher und reduziert die Abhängigkeit von externen Modellaufrufen in normalen Abläufen.

### 9. Betriebsreife hat Vorrang vor weiterer Funktionserweiterung
- Für die nächste Entwicklungsphase ist eine frühzeitige Start- und Konfigurationsprüfung sinnvoller als das Hinzufügen weiterer Features.
- Klar erkennbare Fehlersituationen und saubere Startbedingungen verbessern die Zuverlässigkeit deutlich schneller als neue Endpunkte oder komplexere Logik.

### 10. Sensitive Daten müssen von Beginn an geschützt werden
- Lokale Credentials, Token, Umgebungsdateien und ähnliche Geheimnisse sollten niemals in das Repository gelangen.
- Eine frühe und breite `.gitignore`-Abdeckung reduziert das Risiko von versehentlichen Commits erheblich.
