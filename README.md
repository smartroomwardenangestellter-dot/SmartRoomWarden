# SmartRoomWarden

SmartRoomWarden ist ein Projekt zur automatisierten Raumüberwachung über Kamera-Uploads, Kalenderprüfung und Benachrichtigungen. Ziel ist es, den Status eines Raums zuverlässig zu erkennen und bei Bedarf Hinweise zu erzeugen.

## Projektziel
- Bilder über einen Upload-Endpunkt verarbeiten
- Personen im Raum erkennen
- aktive Termine aus Google Calendar prüfen
- bei Bedarf Benachrichtigungen senden
- den Raumstatus für weitere Nutzung bereitstellen

## Schnellstart für Entwickler

### 1. Repository klonen
```powershell
git clone <repo-url>
cd SmartRoomWarden
```

### 2. Virtuelle Python-Umgebung anlegen
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Falls die Aktivierung in PowerShell blockiert ist, kann vorher folgendes genutzt werden:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 3. Abhängigkeiten installieren
```powershell
python -m pip install -r requirements.txt
```

### 4. Tests ausführen
```powershell
python -m unittest discover -s tests -p 'test_*.py'
```

### 5. Server starten
```powershell
python src/api&flask/room_monitor_server.py
```

## Wichtige Projektstrukturen
- `src/api&flask/room_monitor_server.py` – Haupt-API und Logik für Status/Upload
- `src/ki_zeugs/vision_mock.py` – Bildanalyse und Erkennung
- `src/config.py` und `src/logger.py` – Konfiguration und Logging
- `tests/test_room_monitor_server.py` – zentrale API-Tests
- `docs/dev_notes/` – Projektdokumentation und Entwicklerwissen
- `obsidian/` – aktiver Vault für Projektwissen, Entscheidungen und Arbeitslog

## GitHub-Workflow für Teammitglieder

### Branches
Für neue Arbeit sollte ein eigener Branch angelegt werden:
```powershell
git checkout -b feature/meine-aenderung
```

Gute Namenskonventionen sind:
- `feature/kurzer-name`
- `fix/kurzer-name`
- `docs/kurzer-name`

### Vor der Arbeit
```powershell
git pull origin main
```

### Nach der Arbeit
```powershell
git status
git add .
git commit -m "Kurze, verständliche Commit-Beschreibung"
git push -u origin feature/meine-aenderung
```

### Pull Request
- Nach dem Push einen Pull Request eröffnen
- Kurz beschreiben, was geändert wurde
- Wichtiges testen und ggf. Screenshots oder Hinweise ergänzen

## Wichtige Hinweise für das Projekt
- Neue Python-Bibliotheken immer in `requirements.txt` ergänzen
- Keine Secrets, Tokens oder Credentials im Repo speichern
- Virtuelle Umgebungen und lokale Logs nicht committen
- Bei Änderungen an Architektur, Tests oder Konfiguration die Dokumentation aktualisieren

## Wissensbasis
- `docs/dev_notes/README.md` – zentrale Entwickler- und Projekt-Dokumentation
- `docs/github_guide_for_team.md` – GitHub-Anleitung für neue Teammitglieder
- `obsidian/README.md` – aktiver Vault für Projektwissen, Entscheidungen und Arbeitslog

## Empfehlung für neue Teammitglieder
- Lies zuerst die Projekt-Dokumentation und den Vault
- Nutze die Tests als erste Sicherheitsstufe
- Frag bei Unsicherheit direkt nach, bevor du große Änderungen machst
- Halte Änderungen klein und nachvollziehbar