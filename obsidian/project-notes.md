# Projekt-Notizen

## Fehler-Log

### 2026-07-24: ImportError bei Tests
- Symptom: `ModuleNotFoundError: No module named 'certifi'`
- Ursache: Die Python-Umgebung im Workspace hatte die Abhängigkeit `certifi` nicht installiert.
- Lösung: `certifi` im lokalen Projekt-Environment installieren.
- Verifikation: Nach der Installation lief der Testlauf erneut durch die Projekt-Tests.

## Aktuelle Prioritäten
- Tests wieder lauffähig machen
- Konfiguration und Secrets sauber auslagern
- Bildverarbeitung auf RAM-basierten Workflow umstellen

## Arbeitsregel
- Siehe zentrale Konventionen: [Vault Conventions](02%20Knowledge/Vault%20Conventions.md) — dort steht, dass `requirements.txt` bei neuen Paketen aktualisiert werden muss.
