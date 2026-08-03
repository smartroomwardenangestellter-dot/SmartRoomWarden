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

### 5. Branch- und Release-Strategie für den Prototyp
- `main` bleibt der verifizierte Prototype-Release-Stand
- neue, klar abgegrenzte Roadmap-Phasen werden auf separaten Branches umgesetzt
- der Branch `feature/ops-runbook` dient der Betriebs- und Runbook-Phase ohne das Produktverhalten zu verändern

### 6. Betriebsdokumentationsstrategie
- die Dev-Notes werden als stabile Projekt-Dokumentation gepflegt
- ein Runbook-Prototyp in `docs/dev_notes/operations.md` dokumentiert erste Betriebs-Checks, Fehlerfälle und Recovery-Schritte
- Teammitglieder sollen damit den aktuellen Betriebszustand ohne Code-Risiko nachvollziehen können

### 7. Secrets-Fix und akzeptiertes TLS-Risiko (2026-07-30)
- Prinzip "Keine Secrets im Quellcode" war in `esp32_cam.ino` (WLAN-SSID/Passwort, Device-Token) und `src/config.py` (Hardcoded-Fallbacks für `DEVICE_TOKEN`/`OWN_EMAIL`) verletzt - behoben: ESP32-Secrets liegen jetzt in gitignored `esp32/secrets.h`, `config.py` hat keine Fallbacks mehr
- `client.setInsecure()` in der ESP32-Firmware bleibt bewusst bestehen statt Cert-Pinning einzuführen: der Pi-Server nutzt Flasks `ssl_context="adhoc"` und erzeugt bei jedem Neustart ein neues Self-signed-Zertifikat, wodurch es kein stabiles Zertifikat zum Pinnen gibt. Akzeptiertes Risiko für das LAN-only-Deployment (WPA2-geschütztes Netz); echtes Pinning würde zuerst einen Umbau des Servers auf ein persistentes Zertifikat erfordern
- Weil das Repo öffentlich ist, gelten das alte WLAN-Passwort und der alte Device-Token als kompromittiert (stehen in Commit `4d4a6f1` in der History) - Rotation ist eine offene manuelle Aufgabe, siehe `current_state.md`

### 8. Doku-Konsolidierung: `docs/` als alleinige Projekt-Dokumentation (2026-08-03)
- Zwei parallele interne Doku-Systeme (`docs/dev_notes/` und ein eingebetteter Obsidian-Vault unter `obsidian/`) wurden zusammengeführt - Auslöser war eine bereits dokumentierte Divergenz (siehe die frühere ADR zu "One-Brain vs. Fragmented Docs" im persönlichen Vault des Projektinhabers), verschärft durch echte Redundanz: von ~40 Dateien in `obsidian/` waren nur 2 noch aktuell gepflegt, der Rest reine Duplikate, generisches Vault-Boilerplate oder tote Stubs/Templates
- `docs/` ist ab sofort die einzige technische Dokumentation im Repo. Der eingebettete Vault (`obsidian/`) wurde komplett entfernt, ebenso `docs/dev_notes/internal/` und `system_prompt.md` (reine KI-Arbeitsanweisungen, keine Produkt-Doku) sowie `docs/Sprintplan.md`/`docs/TODOs.md` (vollständig erledigter historischer Sprintplan, siehe `roadmap.md` für die noch offenen Punkte)
- Prozesswissen, das nicht in technische Doku gehört (Lessons Learned, Arbeits-Session-Logs, Agent-Arbeitsweise-Notizen), lebt jetzt im persönlichen Second-Brain-Vault des Projektinhabers, außerhalb dieses Repos - nicht mehr in einer zweiten, parallelen In-Repo-Wissensbasis
