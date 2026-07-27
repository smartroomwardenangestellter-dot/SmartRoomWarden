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

Auf Debian oder Linux kann alternativ auch Folgendes verwendet werden:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Falls die Aktivierung in PowerShell blockiert ist, kann vorher folgendes genutzt werden:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 3. Laufzeitprofil konfigurieren
Für lokale Simulationen und für echte System-Deploys sollten getrennte Konfigurationsprofile verwendet werden:

- `.env` enthält gemeinsame Basiswerte
- `.env.simulation` enthält die lokale Simulationskonfiguration
- `.env.system` enthält die Konfiguration für den echten System-Clone

Ein typischer Start für Simulationen sieht so aus:
```powershell
$env:SMARTROOMWARDEN_RUNTIME_MODE = "simulation"
python -m pip install -r requirements.txt
python -m unittest discover -s tests -p 'test_*.py'
```

Für den echten System-Clone wird stattdessen das passende Laufzeitprofil verwendet:
```powershell
$env:SMARTROOMWARDEN_RUNTIME_MODE = "system"
python src/api_flask/room_monitor_server.py
```

### 4. Abhängigkeiten installieren
```powershell
python -m pip install -r requirements.txt
```

### 5. Tests ausführen
```powershell
python -m unittest discover -s tests -p 'test_*.py'
```

### 6. Server starten
```powershell
python src/api_flask/room_monitor_server.py
```

### 7. Health-Check
Der Server bietet nach dem Start einen einfachen Gesundheitsendpunkt an:
```powershell
curl http://127.0.0.1:5000/health
```
Er antwortet mit `{"status": "ok"}`, sobald die grundlegende Konfiguration verfügbar ist.

## Wichtige Projektstrukturen
- `src/api_flask/room_monitor_server.py` – Haupt-API und Logik für Status/Upload
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