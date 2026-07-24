# System Architecture

## Überblick
Das System besteht aus mehreren klar getrennten Ebenen:
- Eingabe: Kamerabild-Upload über die API
- Verarbeitung: Bildanalyse und Terminprüfung
- Aktion: Benachrichtigung oder Statusantwort

## Hauptkomponenten
- API-Server: verarbeitet Anfragen und steuert den Workflow
- Vision-Modul: erkennt Personen im Bild
- Konfigurationslayer: zentrale Einstellungen und Secrets
- Logging-Layer: beobachtet und protokolliert Ereignisse

## Arbeitsprinzip
1. Ein Bild wird an den Upload-Endpunkt übergeben.
2. Das System analysiert das Bild.
3. Es prüft, ob ein aktiver Termin vorliegt.
4. Je nach Ergebnis wird ein Status zurückgegeben oder eine Benachrichtigung versendet.

## Offene Verbesserungen
- Konfiguration vollständig zentralisieren
- Fehlerfälle explizit abfangen
- Bildpipeline weiter abstrahieren
