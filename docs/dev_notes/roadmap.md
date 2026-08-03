# Dev Notes Roadmap

## Kurzfristig (innerhalb der nächsten Sessions)
- [x] `tests/test_room_monitor_server.py` weiter ausbauen
- [x] `vision_mock.py` testbar machen und zusätzliche Unit-Tests ergänzen
- [x] `src/api&flask/room_monitor_server.py` auf modulare Servicelayer umstellen
- [x] `.gitignore` final prüfen und sichern
- [x] `current_state.md` aktualisieren, sobald sich Architektur ändert
- [x] Startup- und Konfigurationsprüfung als festen Betriebspunkt festhalten und erweitern

## MVP-Prototyp abgeschlossen
- Der erste funktionierende Prototyp ist jetzt auf dem Main-Branch vorhanden.
- Die Kernfunktionen für Upload, Analyse, Statuslogik und Fehlerbehandlung sind in der aktuellen Projektumgebung verifiziert.
- Die aktuelle Verifikation basiert auf dem automatisierten Testlauf mit 12 erfolgreichen Tests.

## Mittelfristig
- [x] vollständige Fehler- und Konfigurationsdokumentation im Dev Notes Bereich
- [ ] `docs/dev_notes/operations.md` für Betriebsanweisungen erstellen
- [ ] Mock- und Staging-Strategien für Google-Integration dokumentieren
- [ ] mögliche Refactorings in `decisions.md` sammeln

## Langfristig
- Infrastruktur- und Deployment-Notizen ergänzen
- Add-on-Dokumente für ESP-Integration und Kamera-Uploads anlegen
- Wartungshandbuch / Runbook-Prototyp in `docs/dev_notes/operations.md`

## Post-MVP-Backlog
- echte Google-Services in einer produktiven Umgebung mit validen Credentials und Token-Handling verifizieren
- Betriebshandbuch und Runbook für Deployment und Wartung abschließen
- ESP- und Kamerapipeline als echte Integrationsstufe dokumentieren
- weitere Stabilitäts- und Observability-Maßnahmen auf Release-Reife ausbauen

## Ergänzende Themen (übernommen aus dem ehemaligen `docs/TODOs.md`, 2026-08-03)
- [ ] Dashboard-Prototyp planen (optional)
- [ ] Betriebsdokumentation und Wartungskonzept starten
- [ ] Informationsflyer/Inhaltsplan erstellen
- [ ] ESP-Flashing-Tool konzipieren
