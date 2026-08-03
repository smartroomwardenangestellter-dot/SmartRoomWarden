# Developer Notes

Diese Wissensbasis dient als zentrale Dokumentation für wichtige Erkenntnisse, Testergebnisse und Architekturentscheidungen des Projekts.

## Zweck
- Alle relevanten Informationen zu `SmartRoomWarden` regelmäßig sammeln
- Testläufe, Probleme und Entscheidungen nachvollziehbar machen
- Eine zentrale Referenz für die zukünftige Weiterentwicklung bieten

## Struktur
- `README.md`: Überblick und Struktur der Dev-Notizen
- `current_state.md`: Aktueller Projektstatus, Architektur und offene Punkte
- `test_runs.md`: Ergebnisse aus Testläufen und Regressionstests
- `decisions.md`: Wichtige Architektur- und Refactoring-Entscheidungen
- `operations.md`: Betriebs- und Runbook-Prototyp für den nächsten Server-Deploy-Schritt
- `quick_links.md`: Relevante Pfade, Umgebungsvariablen und Kommandos

## Pflege
- Jede Änderung am Code oder an der Architektur sollte hier ergänzt werden
- Testläufe werden unter `test_runs.md` dokumentiert
- Wenn neue Erkenntnisse entstehen, werden sie in `current_state.md` und `decisions.md` eingetragen
- Dieses Verzeichnis (`docs/`) ist die einzige und alleinige Projekt-Dokumentation (Stand 2026-08-03). Der frühere eingebettete Obsidian-Vault unter `obsidian/` wurde retiert - er war größtenteils veraltetes Duplikat und generisches Vault-Boilerplate; Prozesswissen und Learnings, die dort lebten, liegen jetzt im persönlichen Second-Brain-Vault des Projektinhabers (außerhalb dieses Repos), nicht mehr hier. Siehe `decisions.md` #8.
