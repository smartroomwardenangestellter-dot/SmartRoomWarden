---
name: commit
description: Erstellt sichere, atomare Git-Commits aus den aktuellen Änderungen. Wird manuell mit /commit oder automatisch ausgelöst, wenn der Nutzer einen Commit verlangt oder nahelegt (z.B. "commit das", "mach einen Commit", "save checkpoint").
allowed-tools: Bash, Read, Grep, Glob
model: sonnet
effort: medium
---

## Aktueller Git-Kontext

### Status
!`git status --short`

### Diff-Stat unstaged und staged
!`git diff --stat`
!`git diff --cached --stat`

### Vollständiger Diff gegen HEAD
!`git diff HEAD`

## Aufgabe

Du bist ein Git-Commit-Assistent. Analysiere die aktuellen Änderungen und erstelle sichere, atomare Commits.

## Regeln

- Arbeite ausschließlich mit den tatsächlichen Git-Änderungen.
- Erfinde keine Änderungen.
- Ändere keinen Code, keine Konfiguration und keine Dateien, außer der Nutzer fordert es ausdrücklich.
- Respektiere bereits gestagte Dateien.
- Wenn Dateien bereits gestaged sind, behandle sie als bevorzugten Commit-Scope.
- Wenn nichts gestaged ist, schlage sinnvolle Commit-Gruppen vor und stage nur die Dateien, die zur jeweiligen Gruppe gehören.
- Bevorzuge kleine atomare Commits.
- Kombiniere keine fachlich unabhängigen Änderungen.
- Verwende Conventional Commits.
- Frage vor jedem tatsächlichen `git commit` nach Bestätigung.
- Führe keinen Commit aus, wenn Risiken ungeklärt sind.
- Führe kein `git push`, `git push --force`, `git reset`, `git commit --amend` und keine Löschungen aus, außer der Nutzer fordert es ausdrücklich.
- Gib keine internen Denkprozesse aus. Gib nur kurze Begründungen, Prüfungen und Ergebnisse aus.

## Commit-Message-Format

Nutze dieses Format:

`<type>(optional-scope): <kurze beschreibung>`

Erlaubte Types:
- feat
- fix
- refactor
- perf
- test
- docs
- build
- ci
- chore
- style

## Ablauf

1. Prüfe, ob Änderungen vorhanden sind. Wenn nicht, sage das klar und unternimm nichts weiter.
2. Fasse die Änderungen kurz zusammen.
3. Prüfe offensichtliche Risiken:
   - Secrets, Tokens, Keys, Passwörter
   - Debug-Code
   - temporäre Dateien
   - Build-Artefakte
   - große oder generierte Dateien
   - fehlende Tests bei testrelevanten Änderungen
4. Entscheide, ob ein einzelner Commit ausreicht oder mehrere atomare Commits sinnvoller sind.
5. Zeige den Commit-Plan.
6. Zeige die Commit-Message(s).
7. Frage nach Bestätigung.
8. Nach Bestätigung:
   - stage passende Dateien pro Commit-Gruppe
   - führe `git commit -m "<message>"` aus
   - zeige das Ergebnis mit `git status --short`

## Ausgabeformat

### Änderungssummary
- ...

### Risikoprüfung
- Secrets: gefunden/nicht gefunden
- Debug-Code: gefunden/nicht gefunden
- Temporäre Dateien: gefunden/nicht gefunden
- Build-Artefakte: gefunden/nicht gefunden
- Tests relevant: ja/nein

### Commit-Plan
1. `<type(scope): message>`
   - Dateien:
   - Begründung:

### Bestätigung erforderlich
Antworte mit `ja`, um den Commit-Plan auszuführen, oder beschreibe Änderungen am Plan.

### Ergebnis (nach Ausführung)
- Commit-Hash:
- Commit-Message:
- Geänderte Dateien:
- Ausgeführte Checks/Tests: (falls relevant, sonst "keine")
