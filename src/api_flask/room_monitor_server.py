# -*- coding: utf-8 -*-

import os
import sys
import base64
import hmac

from flask import Flask, request, Response, jsonify
from email.mime.text import MIMEText
from datetime import datetime, timezone

try:
    import certifi
except ImportError:  # pragma: no cover - optional runtime dependency
    certifi = None

if certifi is not None:
    os.environ["SSL_CERT_FILE"] = certifi.where()
    os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError:  # pragma: no cover - optional runtime dependency
    Request = None
    Credentials = None
    InstalledAppFlow = None
    build = None

from pathlib import Path

# Pfade konfigurieren
BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR.parent
sys.path.insert(0, str(SRC_DIR))

from config import GOOGLE_CREDENTIALS_PATH, GOOGLE_TOKEN_PATH, DEVICE_TOKEN, OWN_EMAIL
from ki_zeugs.vision_mock import check_raum_status, get_model
from logger import get_logger, setup_logging

SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/gmail.send"
]

# ----------------------------------------

setup_logging()
logger = get_logger("room_monitor_server")

app = Flask(__name__)


MODEL_CACHE = {}


def validate_configuration():
    issues = []

    if not DEVICE_TOKEN:
        issues.append("Device token is not configured")

    if not OWN_EMAIL:
        issues.append("Own email is not configured")

    if not GOOGLE_CREDENTIALS_PATH.exists():
        issues.append("Google credentials file not found")

    if not GOOGLE_TOKEN_PATH.exists():
        issues.append("Google token file not found")

    return issues


configuration_issues = validate_configuration()
if configuration_issues:
    logger.warning("Konfigurationsprüfung fehlgeschlagen: %s", ", ".join(configuration_issues))


def get_credentials():
    if Credentials is None or Request is None or InstalledAppFlow is None:
        raise RuntimeError("Google client libraries are not available")

    creds = None

    if GOOGLE_TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(
            str(GOOGLE_TOKEN_PATH),
            SCOPES,
        )

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not GOOGLE_CREDENTIALS_PATH.exists():
                logger.error(f"Credentials-Datei nicht gefunden: {GOOGLE_CREDENTIALS_PATH}")
                raise FileNotFoundError(
                    f"Google credentials not found: {GOOGLE_CREDENTIALS_PATH}"
                )

            flow = InstalledAppFlow.from_client_secrets_file(
                str(GOOGLE_CREDENTIALS_PATH),
                SCOPES,
            )
            creds = flow.run_local_server(port=0)

        GOOGLE_TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(GOOGLE_TOKEN_PATH, "w") as token:
            token.write(creds.to_json())

    return creds


def get_services():
    if build is None:
        raise RuntimeError("Google client libraries are not available")

    issues = validate_configuration()
    if issues:
        joined_issues = ", ".join(issues)
        logger.error("Google-Dienste nicht verfügbar: %s", joined_issues)
        raise RuntimeError(f"Google services unavailable: {joined_issues}")

    creds = get_credentials()

    calendar_service = build(
        "calendar",
        "v3",
        credentials=creds,
    )

    gmail_service = build(
        "gmail",
        "v1",
        credentials=creds,
    )

    return calendar_service, gmail_service


def send_email(gmail_service, to_email, subject, body):
    message = MIMEText(body, "plain", "utf-8")
    message["to"] = to_email
    message["subject"] = subject

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    gmail_service.users().messages().send(
        userId="me",
        body={"raw": raw_message},
    ).execute()


def token_ok():
    token = request.headers.get("X-Device-Token", "")

    if not DEVICE_TOKEN or not hmac.compare_digest(token, DEVICE_TOKEN):
        logger.warning("Falscher oder fehlender Device-Token")
        return False

    return True


def get_cached_model():
    if "vision" not in MODEL_CACHE:
        MODEL_CACHE["vision"] = get_model()
    return MODEL_CACHE["vision"]


def get_server_config():
    host = os.getenv("SMARTROOMWARDEN_HOST", "0.0.0.0")
    port = int(os.getenv("SMARTROOMWARDEN_PORT", "5000"))
    ssl_enabled = os.getenv("SMARTROOMWARDEN_SSL", "false").lower() in {"1", "true", "yes", "on"}
    ssl_context = "adhoc" if ssl_enabled else None
    return host, port, ssl_context


def get_current_event(calendar_service):
    now_utc = datetime.now(timezone.utc)
    now_iso = now_utc.isoformat()

    events_result = (
        calendar_service.events()
        .list(
            calendarId="primary",
            timeMin=now_iso,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get("items", [])

    for event in events:
        start = event["start"].get(
            "dateTime",
            event["start"].get("date"),
        )

        end = event["end"].get(
            "dateTime",
            event["end"].get("date"),
        )

        start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
        end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))

        if start_dt <= datetime.now(timezone.utc) <= end_dt:
            return event, start_dt

    return None, None


@app.route("/health", methods=["GET"])
def health():
    issues = validate_configuration()
    if issues:
        return jsonify({"status": "error", "issues": issues}), 503

    return jsonify({"status": "ok"})


@app.route("/status", methods=["GET"])
def status():
    if not token_ok():
        return Response("unauthorized", status=401)

    try:
        calendar_service, _ = get_services()
        event, _ = get_current_event(calendar_service)
    except Exception:
        logger.exception("Status-Abfrage fehlgeschlagen")
        return Response("Dienst nicht verfügbar", status=503)

    if event:
        logger.info("Termin aktiv")
        return Response("true", mimetype="text/plain")

    logger.info("Kein Termin")
    return Response("false", mimetype="text/plain")


MAX_UPLOAD_BYTES = 10 * 1024 * 1024


@app.route("/upload", methods=["POST"])
def upload():
    if not token_ok():
        return Response("unauthorized", status=401)

    if request.content_length is not None and request.content_length > MAX_UPLOAD_BYTES:
        logger.warning("Upload überschreitet die maximale Größe (%s Bytes)", request.content_length)
        return Response("Bild zu groß", status=413)

    if request.content_type and not request.content_type.startswith("image/"):
        logger.warning("Upload mit unerwartetem Content-Type erhalten: %s", request.content_type)
        return Response("Ungültiger Content-Type", status=415)

    try:
        calendar_service, gmail_service = get_services()
        event, start_dt = get_current_event(calendar_service)
    except Exception:
        logger.exception("Upload-Initialisierung fehlgeschlagen")
        return Response("Dienst nicht verfügbar", status=503)

    try:
        if not event:
            return Response("Kein aktiver Termin", status=200)

        image_bytes = request.get_data()
        if not image_bytes:
            logger.warning("Upload ohne Bilddaten erhalten")
            return Response("Kein Bild", status=400)

        logger.info("Bild empfangen, starte Analyse")
        model = get_cached_model()
        raum_besetzt = check_raum_status(image_bytes, model=model)

        if raum_besetzt:
            logger.info("Raum besetzt")
            return Response("Raum besetzt", status=200)

        if start_dt is None:
            logger.error("Aktiver Termin ohne Startzeit gefunden")
            return Response("Server Fehler", status=500)

        termin_laeuft_seit = datetime.now(timezone.utc) - start_dt
        if termin_laeuft_seit.total_seconds() < 10 * 60:
            logger.info("Raum leer, aber Termin läuft noch keine 10 Minuten")
            return Response("Termin läuft noch keine 10 Minuten", status=200)

        logger.info("Raum leer und Termin läuft seit mindestens 10 Minuten -> Mail senden")
        title = event.get("summary", "(Kein Titel)")
        attendees = event.get("attendees", [])

        for attendee in attendees:
            email = attendee.get("email", "")
            if not email:
                continue
            if OWN_EMAIL and email.lower() == OWN_EMAIL.lower():
                continue

            subject = f"Raumfreigabe prüfen: {title}"
            body = f"""
Hallo,

du hast aktuell einen Raum für das Meeting {title} gebucht.
In dem Raum befinden sich derzeit keine Personen.

Bitte denk dran Räume wieder frei zu geben, falls diese doch nicht benötigt werden, 
oder Termine verschoben werden, damit sie für andere Termine genutz werden können.

Vielen Dank!

Smart Room Warden
"""

            try:
                send_email(
                    gmail_service,
                    email,
                    subject,
                    body,
                )
                logger.info(f"Mail gesendet an {email}")
            except Exception:
                logger.exception(f"Fehler beim Senden der E-Mail an {email}")

        return Response("Fertig", status=200)

    except Exception:
        logger.exception("Unerwarteter Fehler im Upload-Endpoint")
        return Response("Server Fehler", status=500)


if __name__ == "__main__":
    host, port, ssl_context = get_server_config()
    app.run(
        host=host,
        port=port,
        ssl_context=ssl_context,
    )
