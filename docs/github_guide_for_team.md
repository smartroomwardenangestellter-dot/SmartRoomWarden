# GitHub-Anleitung für Teammitglieder

Diese Anleitung beschreibt den Standard-Workflow für Zusammenarbeit im Projekt SmartRoomWarden. Sie ist bewusst praxisnah aufgebaut und auf Teammitglieder zugeschnitten, die Git und GitHub noch nicht täglich verwenden.

## 1. Arbeitsgrundlage

Für jede Änderung wird ein eigener Branch verwendet. Das sorgt für saubere, nachvollziehbare und einfache Zusammenarbeit.

### Grundregeln
- Arbeiten immer in einem eigenen Branch
- Änderungen klein und verständlich halten
- Vor dem Commit prüfen, ob nur die beabsichtigten Dateien geändert wurden
- Bei Unsicherheit zuerst nachfragen, statt unkontrolliert zu verändern

## 2. Repository vorbereiten

### Repository klonen
```powershell
git clone <repo-url>
cd SmartRoomWarden
```

### Aktuellen Stand abrufen
```powershell
git pull origin main
```

## 3. Branch-Strategie

### Neuen Branch anlegen
```powershell
git checkout -b feature/meine-aenderung
```

### Beispiele für Branch-Namen
- `feature/raumstatus-api`
- `fix/test-import`
- `docs/readme-update`
- `chore/dependencies`

## 4. Änderungen prüfen

Vor dem Speichern sollten die Änderungen immer kontrolliert werden:
```powershell
git status
git diff
```

Damit lässt sich schnell erkennen:
- welche Dateien geändert wurden
- ob unerwartete Änderungen vorhanden sind
- ob nur die beabsichtigten Änderungen Teil des Commits sind

## 5. Änderungen committen

### Dateien vorbereiten
```powershell
git add .
```

### Commit erstellen
```powershell
git commit -m "Kurze und präzise Commit-Beschreibung"
```

### Gute Commit-Regeln
- kurz und konkret
- verständlich für andere Teammitglieder
- nicht zu allgemein

Beispiele:
- `Add project vault documentation`
- `Fix test import for certifi`
- `Update README with setup instructions`

## 6. Änderungen hochladen

```powershell
git push -u origin feature/meine-aenderung
```

## 7. Pull Request erstellen

Nach dem Push wird ein Pull Request eröffnet:
1. In GitHub zum Repository gehen
2. Den neuen Branch auswählen
3. Auf „Compare & pull request“ klicken
4. Kurz beschreiben:
   - was geändert wurde
   - warum die Änderung nötig war
   - ob Tests ausgeführt wurden
   - ob weitere Hinweise relevant sind

### Gute PR-Beschreibung
```text
Änderung: Beschreibung der Änderung
Grund: Warum wurde sie umgesetzt?
Test: Welche Tests wurden ausgeführt?
```

## 8. Projektregeln für SmartRoomWarden

Diese Regeln sollten immer eingehalten werden:
- Neue Python-Bibliotheken immer in `requirements.txt` eintragen
- Keine Secrets, Tokens oder Credentials im Repository speichern
- Keine lokalen virtuellen Umgebungen oder Logs committen
- Bei Änderungen an Architektur, Konfiguration oder Tests die Dokumentation mit aktualisieren
- Kleine, nachvollziehbare Änderungen bevorzugen

## 9. Häufig verwendete Befehle

```powershell
git pull origin main
git status
git add .
git commit -m "..."
git push -u origin feature/meine-aenderung
```

## 10. Wenn etwas schiefgeht

Falls ein Commit oder Push nicht funktioniert, hilft oft zuerst der Status-Check:
```powershell
git status
git log --oneline -5
```

Wenn Unsicherheit besteht, sollte lieber kurz nachgefragt werden, statt ohne Kontrolle Änderungen vorzunehmen.

## 11. Empfohlener Arbeitsablauf

Ein typischer Ablauf sieht so aus:
1. Repository klonen oder aktualisieren
2. Neuen Branch anlegen
3. Änderungen entwickeln
4. `git status` und `git diff` prüfen
5. Commit erstellen
6. Pushen
7. Pull Request öffnen

Dieser Ablauf ist für das Projekt geeignet, weil er sauber, transparent und für neue Teammitglieder leicht nachvollziehbar ist.
