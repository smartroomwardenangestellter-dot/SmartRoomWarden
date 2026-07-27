# Betriebs- und Runbook-Prototyp

## Ziel

Dieses Dokument bildet den ersten Betriebs- und Runbook-Startpunkt für SmartRoomWarden für den nächsten Deploy-Schritt auf einem Zielserver.

Im Fokus stehen:
- sauberer Start und Verifikation der Umgebung
- nachvollziehbare Konfigurationschecks
- einfache Betriebsprüfungen über Health- und Status-Endpoints
- erste Hinweise für Fehlerfälle, Recovery und Nachvollziehbarkeit

## Aktueller Status

Der Prototyp ist lokal mit Tests verifiziert. Die nächste Phase konzentriert sich auf Betriebssicherheit, Dokumentation und Deploy-Ready-Konfiguration.

## Arbeitsumgebung

### Python-Umgebung

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Bei Bedarf kann die PowerShell-Policy vorübergehend angepasst werden:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Abhängigkeiten

```powershell
python -m pip install -r requirements.txt
```

## Betriebsvorbereitung

### 1. Umgebung prüfen

Vor dem Start sollten diese Punkte erfüllt sein:
- virtuelle Umgebung ist aktiv
- Abhängigkeiten sind installiert
- die Konfigurationsdateien für das gewünschte Profil liegen vor
- Secrets und Token liegen nur lokal und nicht im Repository

### 2. Tests ausführen

```powershell
python -m unittest discover -s tests -p 'test_*.py'
```

Aktueller Stand: 19 Tests erfolgreich.

### 3. Server starten

```powershell
python src/api_flask/room_monitor_server.py
```

### 4. Nach dem Start prüfen

- `/health` sollte mit `{"status": "ok"}` antworten, wenn die Grundkonfiguration vorhanden ist
- `/status` sollte einen klaren Zustand liefern
- Upload- und Mail-Mechanik sollten sauber protokolliert werden

## Konfigurationsprinzipien

Wichtige Regeln:
- keine Secrets direkt im Code
- lokale Credentials und Token-Dateien nicht versionieren
- Konfigurationswerte über Umgebungsvariablen oder lokale Profil-Dateien steuern
- bei fehlenden Google-Credentials sauber auf einen degradierten Zustand reagieren

## Wichtige Umgebungsvariablen

- `SMARTROOMWARDEN_DEVICE_TOKEN`
- `SMARTROOMWARDEN_OWN_EMAIL`
- `GOOGLE_CREDENTIALS_PATH`
- `GOOGLE_TOKEN_PATH`
- `SMARTROOMWARDEN_HOST`
- `SMARTROOMWARDEN_PORT`
- `SMARTROOMWARDEN_SSL`

## Betriebschecks

### Erwartete Laufzeitindikatoren

- Logs im `logs/`-Ordner sind vorhanden
- Konfigurationsprüfung wird sauber protokolliert
- Uploads und Bildanalysen erscheinen als nachvollziehbare Ereignisse
- Fehler bei Google- oder Mail-Integration sind sichtbar und nicht stillschweigend

### Erwartete Fehlerfälle

Diese Situationen sind für den aktuellen Prototyp normal und sollten sauber behandelt werden:
- fehlende Google-Credentials oder Token-Dateien
- ungültige oder leere Bilddaten
- temporäre externe Dienstfehler

## Recovery und Wiederanlauf

1. Umgebung aktivieren
2. Abhängigkeiten prüfen
3. Tests erneut ausführen
4. Server neu starten
5. Health-/Status-Checks erneut ausführen

## Nächste Schritte

- echte Google-/Mail-Integration auf dem Zielserver verifizieren
- Deploy- und Reverse-Proxy-Konfiguration für Debian 13 vorbereiten
- Runbook um reale Betriebsbeobachtungen erweitern
