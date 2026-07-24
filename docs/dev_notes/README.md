# Developer Notes

Diese Wissensbasis dient als zentrale Dokumentation für wichtige Erkenntnisse, Testergebnisse und Architekturentscheidungen des Projekts.

## Zweck
- Alle relevanten Informationen zu `SmartRoomWarden` regelmäßig sammeln
- Testläufe, Probleme und Entscheidungen nachvollziehbar machen
- Eine zentrale Referenz für die zukünftige Weiterentwicklung bieten

## Struktur
- `README.md`: Überblick und Struktur der Dev-Notizen
- `system_prompt.md`: Arbeitsanweisung für die AI zur Nutzung dieses Bereichs
- `current_state.md`: Aktueller Projektstatus, Architektur, offene Probleme
- `test_runs.md`: Ergebnisse aus Testläufen und Regressionstests
- `decisions.md`: Wichtige Architektur- und Refactoring-Entscheidungen
- `roadmap.md`: Fokus, Prioritäten und geplante Schritte
- `operations.md`: Betriebs- und Runbook-Prototyp für den ersten operativen Nutzungskontext
- `quick_links.md`: Relevante Pfade, Umgebungsvariablen, Kommandos
- `internal/`: AI-interne Arbeitsdokumente und Cleanup-Notizen

## Pflege
- Jede Änderung am Code oder an der Architektur sollte hier ergänzt werden
- Testläufe werden unter `test_runs.md` dokumentiert
- Wenn neue Erkenntnisse entstehen, werden sie in `current_state.md` und `decisions.md` eingetragen
- Dieses Verzeichnis bleibt die stabile Projekt-Dokumentation; der lokale Obsidian-Vault unter `obsidian/` ist die aktive Arbeits- und Wissensbasis
