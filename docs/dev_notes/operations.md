# Betriebs- und Runbook-Prototyp

## Ziel

Dieses Dokument bildet den ersten Betriebs- und Runbook-Startpunkt für SmartRoomWarden auf dem Roadmap-Branch `feature/ops-runbook`.

Der Fokus liegt auf einer nachvollziehbaren, klein gehaltenen Betriebsbasis für den bereits verifizierten Prototyp-MVP:

- Start und Verifikation der Projektumgebung
- notwendige Konfigurationschecks
- Bewertung des Laufzeitstatus
- sichere Hinweise für erste operative Nutzung und Nachverfolgung

## Aktueller Status

Der Prototyp ist im `main`-Branch verifiziert. Die nächste Roadmap-Phase erweitert die Betriebssicherheit durch zentrale Dokumentation statt durch neue Produktlogik.

## Arbeitsumgebung

### Python-Umgebung

Das Projekt wird in einer lokalen virtuellen Umgebung erwartet:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Falls PowerShell die Aktivierung blockiert, kann vorübergehend der Prozess-Policy-Bypass genutzt werden:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Abhängigkeiten

```powershell
python -m pip install -r requirements.txt
```

## Grundgerüst für den Betrieb

### 1. Verifikation der Umgebung

Vor dem Start sollte sichergestellt sein:

- die virtuelle Umgebung ist aktiv
- `requirements.txt` ist installiert
- der Code wird mit dem Projekt-Interpreter gestartet
- keine lokalen Secrets oder Tokens werden im Repo abgelegt

### 2. Test-Check

```powershell
python -m unittest discover -s tests -p 'test_*.py'
```

Der erwartete Verifikationsstand für den aktuellen Prototyp ist:

- 12 Tests ausgeführt
- alle Tests erfolgreich (`OK`)

### 3. Start des Servers

```powershell
python src/api&flask/room_monitor_server.py
```

## Konfigurationsprinzipien

Die zentrale Konfiguration wird über die Projektdateien `src/config.py` und `src/logger.py` abgewickelt.

Wichtige Regeln:

- keine Secrets direkt im Code
- lokale Credentials und Token-Dateien nicht versionieren
- Konfigurationsprüfungen vor dem Betrieb ausführen
- beim Fehlen von Google-Credentials sauber auf eine degradierte Betriebsform reagieren

## Erste Betriebs-Checks

Nach dem Start sollten die folgenden Punkte kontrolliert werden:

1. Server startet ohne Importfehler
2. `/status` liefert einen klaren Antwortstatus
3. Upload-Handling tritt sauber auf, falls Bilder fehlen oder ungültig sind
4. Fehler werden in den Logs mit klarer Ursache dokumentiert
5. die Google-Integration bleibt beim Fehlen lokaler Credentials nicht abrupt am Server hängen

## Logging und Nachverfolgung

Das Projekt nutzt zentralisiertes Logging. Für den ersten Betriebsrahmen gelten diese Erwartungen:

- Start und Konfigurationsprüfung sollen nachvollziehbar geloggt werden
- Upload- und Analyseaktivitäten sollen als Ereignisse sichtbar sein
- fehlgeschlagene Google-Services und Mail-Versandfälle müssen eindeutig erkennbar sein

## Erste Laufzeit- und Fehlerbeobachtung

### Erwartete Fehlerfälle

Die folgende Situation ist im Prototyp bereits vorgesehen und darf in der frühen Betriebsphase normal auftreten:

- fehlende Google-Credentials oder Token-Dateien
- ungültige oder leere Bilddaten
- ausgelagerte Google-Service-Fehler bei fehlender Realintegration

### Erwartete Antwortmuster

- `503` oder andere saubere Service-Fehler bei fehlender Konfiguration bzw. fehlgeschlagenem Service-Layer
- klare Log-Meldungen statt stillschweigende Ausfälle
- keine unkontrollierten Crashes beim Fehlen externer Ressourcen

## Post-MVP-Backlog für den nächsten Schritt

Die folgenden Punkte bleiben für die eigentliche Release-Reife offen:

- echte Google-Services in einer produktiven Umgebung verifizieren
- Voll-Runbook für Deployment und Wiederanlauf erstellen
- ESP- und Kamera-Integrationsdokumentation ergänzen
- weitere Betriebs- und Observability-Maßnahmen im echten Umgebungsbetrieb aufbauen

## Arbeitsnotiz für diesen Branch

Dieser Branch dient dazu, Betriebs- und Runbook-Abschnitte gezielt zu dokumentieren, ohne die Prototyp-Logik selbst weiter zu verändern. Die Doku ist hier das primäre Produkt des Workstreams.
