# Cleanup Plan

## Ziel
Dieser Plan beschreibt, wie du den `docs/dev_notes/`-Bereich intern strukturierst und sauber hältst.

## Schritte
1. Behalte nur essentielle Dateien im Hauptordner:
   - `README.md`
   - `system_prompt.md`
   - `current_state.md`
   - `decisions.md`
   - `test_runs.md`
   - `roadmap.md`
   - `quick_links.md`
2. Lege interne Arbeitsdateien in `internal/` ab.
3. Vermeide redundante Details im Hauptordner.
4. Aktualisiere `README.md` so, dass die Struktur klar ist.

## Aktueller Status
- `system_prompt.md` ist eingerichtet.
- Es gibt einen neuen internen Ordner für AI-spezifische Dokumentation.
- Die Hauptdateien bleiben sichtbar, aber interne Logik gehört in `internal/`.

## Nächste Pflege-Aufgabe
- Überprüfe regelmäßig, ob `current_state.md` und `decisions.md` noch sinnvoll getrennt sind.
- Wenn `roadmap.md` operativ wird, verschiebe den detaillierten Plan nach `internal/`.
