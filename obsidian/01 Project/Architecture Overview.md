# Architecture Overview

## Überblick
- Frontend/Client: ESP32-Kamera und Upload-Mechanik
- Backend: Flask-Server für Status und Upload
- Bildanalyse: YOLO-basierte Erkennung über Vision-Modul
- Integration: Google Calendar und Gmail

## Komponenten
- API-Server: `src/api&flask/room_monitor_server.py`
- Vision: `src/ki_zeugs/vision_mock.py`
- Konfiguration: `src/config.py`
- Logging: `src/logger.py`

## Offene Architekturfragen
- Wie werden Secrets sicher verwaltet?
- Wie wird die Konfiguration vollständig zentralisiert?
- Wie wird die Bildpipeline weiter abstrahiert?
