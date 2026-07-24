# Project Context

## Überblick
SmartRoomWarden ist ein Projekt zur automatisierten Erkennung leerer oder besetzter Räume über Bildanalyse, Kalender- und Benachrichtigungslogik.

## Ziel des Systems
- Räume anhand von Kamerabilddaten analysieren
- aktive Termine aus Google Kalender prüfen
- bei Bedarf Benachrichtigungen versenden
- den Raumstatus für das Monitoring verfügbar machen

## Kernelemente
- Flask-API für Status- und Upload-Endpunkte
- Bildanalyse über ein Vision-Modul
- Konfiguration für Tokens, Pfade und E-Mail-Integration
- Logging und Fehlerbehandlung als zentrale Infrastruktur

## Wichtige Annahmen
- Die Bildverarbeitung soll effizient und ohne unnötige Dateizwischenschritte erfolgen.
- Externe Dienste sollten testbar und isoliert nutzbar sein.
- Der Vault soll die Projektkonsistenz und das Wissen über die Architektur sichern.
