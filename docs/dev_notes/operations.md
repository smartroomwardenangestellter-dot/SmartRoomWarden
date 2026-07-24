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

### 4. Start-Sequenz für den ersten Betrieb

1. In das Projekt-Verzeichnis wechseln.
2. Die virtuelle Umgebung aktivieren.
3. Abhängigkeiten prüfen und falls nötig installieren.
4. Tests ausführen, bevor der Server gestartet wird.
5. Den Server mit dem Projekt-Interpreter starten.
6. Nach dem Start den Health-/Statuspfad prüfen.

### 5. Checkliste nach dem Start

- Der Flask-Server ist ohne Importfehler hochgefahren.
- Die Konfigurationsprüfung läuft ohne unerwartete Abbrüche.
- Die Logs zeigen keine kritischen Fehlermeldungen zum Start.
- Der Status-Endpunkt ist erreichbar und signalisiert den erwarteten Zustand.

## Betriebskontrolle und Monitoring

### Wichtige Laufzeitindikatoren

Für die erste operative Nutzung sind die folgenden Punkte relevant:

- die Logausgabe im `logs/`-Ordner
- das Verhalten bei fehlenden Google-Credentials
- das Verhalten bei leeren, ungültigen oder nicht dekodierbaren Bilddaten
- die Mail-/Benachrichtigungslogik bei aktiver Zeitplanung

### Erwartete Logs

Menschen, die den Server betreiben, sollten in den Logdateien die folgenden Ereignisklassen erkennen:

- Systemstart
- Konfigurationsprüfung
- Upload und Bildanalyse
- Kalender- oder Terminstatus
- Benachrichtigungssendungen
- Fehler bei Google-Service- oder Mail-Laufzeit

## Fehlerfall- und Recovery-Protokoll

### Problem: fehlende Google-Credentials oder Token

Symptom:

- die Konfigurationsprüfung meldet fehlende Dateien
- der Server läuft in eine degradierte Form, statt komplett abzubrechen

Maßnahme:

- den Betrieb nur mit validen lokalen Credentials fortsetzen
- die fehlenden Dateien nicht in das Repository aufnehmen
- die Ursache im Log nachvollziehbar dokumentieren

### Problem: kein oder ungültiges Bild

Symptom:

- Upload kommt an, aber die Bilddekodierung schlägt fehl
- der Server dokumentiert den Fehler sauber und setzt den Lauf fort

Maßnahme:

- das Bild erneut senden oder die Aufnahme überprüfen
- die Log-Ausgabe zur Ursache lesen
- den Ablauf nicht als Crash interpretieren

### Problem: Service- oder Google-Request-Fehler

Symptom:

- der Dienst ist nicht erreichbar oder meldet Laufzeitfehler
- der Status-Endpunkt reagiert mit sauberem Fehlerverhalten

Maßnahme:

- den Fehler im Log nachvollziehen
- die betroffene Integration als externen Service behandeln
- den weiteren Betrieb nicht durch ein unkontrolliertes Abbrechen unterbrechen

## Stopp- und Wiederanlauf-Prozess

### Sicherer Stop

Der Server sollte mit einem kontrollierten Abbruch beendet werden. Für den ersten Prototyp ist der wichtigste Punkt die saubere Beendigung ohne beschädigte Log- oder Prozesszustände.

### Wiederanlauf

Bei einem Wiederanlauf sind diese Schritte entscheidend:

1. Umgebung wieder aktivieren
2. Abhängigkeiten prüfen
3. Tests ausführen
4. Server neu starten
5. Nachstart-Checks erneut durchführen

## Team-Workflow für die Betriebsphase

- Änderungen an Server-, Config- oder Logging-Verhalten dokumentieren
- wichtige Betriebsbeobachtungen in den Dev Notes aufnehmen
- neue Fehlerfälle in diesem Runbook ergänzen
- bei echten Google- oder Mail-Integrationsproblemen den Betrieb als separate Problemphase behandeln

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
