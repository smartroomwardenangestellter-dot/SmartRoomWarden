# Decision Log

Chronologische Aufzeichnung aller Entscheidungen und relevanter Kontext-Notizen. Verwenden Sie dieses Log als die primäre Quelle für "was, wann, warum".

## 2026-07-24
- Der Obsidian-Vault wird als aktive Wissens- und Arbeitsbasis für SmartRoomWarden genutzt.
- Dev-Notes und Vault werden zusammengeführt, statt getrennt weiterzuentwickeln.
- Fehlerlösungen werden explizit dokumentiert, nicht nur notiert.

## 2026-07-30
- Hardcoded Secrets entfernt: WLAN-SSID/Passwort und Device-Token aus `esp32_cam.ino` in gitignored `esp32/secrets.h` ausgelagert; Hardcoded-Fallbacks für `DEVICE_TOKEN`/`OWN_EMAIL` aus `src/config.py` entfernt.
- `client.setInsecure()` (TLS) bewusst als akzeptiertes Risiko dokumentiert statt Cert-Pinning einzuführen - der Pi-Server nutzt `ssl_context="adhoc"` (Zertifikat wechselt bei jedem Neustart), echtes Pinning würde erst einen Server-Umbau erfordern.
- Repo ist öffentlich auf GitHub - altes WLAN-Passwort und Device-Token stehen weiterhin in der Git-History (Commit `4d4a6f1`) und gelten als kompromittiert. Rotation (Router-Passwort, Device-Token + ESP32 neu flashen) und Git-History-Bereinigung sind offene manuelle Schritte, siehe `docs/dev_notes/current_state.md`.
