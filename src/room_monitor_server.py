-- coding: utf-8 --

import osimport sysimport certifiimport base64

from flask import Flask, request, Responsefrom email.mime.text import MIMETextfrom datetime import datetime, timezone

os.environ["SSL_CERT_FILE"] = certifi.where()os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

from google.auth.transport.requests import Requestfrom google.oauth2.credentials import Credentialsfrom google_auth_oauthlib.flow import InstalledAppFlowfrom googleapiclient.discovery import build

vision_mock importieren

sys.path.append("/home/smartroomwarden/SRW/OKI_Darian")

from vision_mock import check_raum_status

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly","https://www.googleapis.com/auth/gmail.send"]

OWN_EMAIL = "removed-email@example.invalid"

DEVICE_TOKEN = "***REMOVED-DEVICE-TOKEN***"

def token_ok():# Wir holen uns den Token, den der ESP32 im Header versteckt haterhaltener_token = request.headers.get('X-Device-Token')

# Wir prüfen, ob er exakt mit unserem Passwort übereinstimmt
if erhaltener_token == "***REMOVED-DEVICE-TOKEN***":
    return True
else:
    print("Sicherheitswarnung: Falscher oder fehlender Token!")
    return False

----------------------------------------

Bildspeicherort

VISION_BILD = "/home/smartroomwarden/SRW/OKI_Darian/room.jpg"

app = Flask(name)

def get_credentials():

creds = None

if os.path.exists("token.json"):

    creds = Credentials.from_authorized_user_file(
        "token.json",
        SCOPES
    )

if not creds or not creds.valid:

    if creds and creds.expired and creds.refresh_token:

        creds.refresh(Request())

    else:

        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            SCOPES
        )

        creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
        token.write(creds.to_json())

return creds

def get_services():

creds = get_credentials()

calendar_service = build(
    "calendar",
    "v3",
    credentials=creds
)

gmail_service = build(
    "gmail",
    "v1",
    credentials=creds
)

return calendar_service, gmail_service

def send_email(gmail_service, to_email, subject, body):

message = MIMEText(body, "plain", "utf-8")

message["to"] = to_email
message["subject"] = subject

raw_message = base64.urlsafe_b64encode(
    message.as_bytes()
).decode()

gmail_service.users().messages().send(
    userId="me",
    body={"raw": raw_message}
).execute()

def token_ok():

token = request.headers.get("X-Device-Token", "")

return token == DEVICE_TOKEN

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
        event["start"].get("date")
    )

    end = event["end"].get(
        "dateTime",
        event["end"].get("date")
    )

    start_dt = datetime.fromisoformat(
        start.replace("Z", "+00:00")
    )

    end_dt = datetime.fromisoformat(
        end.replace("Z", "+00:00")
    )

    if start_dt <= datetime.now(timezone.utc) <= end_dt:
        return event, start_dt

return None, None

@app.route("/status", methods=["GET"])def status():

if not token_ok():
    return Response("unauthorized", status=401)

calendar_service, _ = get_services()

event, start_dt = get_current_event(calendar_service)

if event:
    print("Termin aktiv")
    return Response("true", mimetype="text/plain")

print("Kein Termin")

return Response("false", mimetype="text/plain")

@app.route("/upload", methods=["POST"])def upload():

if not token_ok():
    return Response("unauthorized", status=401)

try:

    calendar_service, gmail_service = get_services()

    event, start_dt = get_current_event(calendar_service)

    if not event:
        return Response("Kein aktiver Termin", status=200)

    image_bytes = request.get_data()

    if not image_bytes:
        return Response("Kein Bild", status=400)

    # Bild speichern
    with open(VISION_BILD, "wb") as f:
        f.write(image_bytes)

    print("Bild gespeichert")

    # KI Analyse
    raum_besetzt = check_raum_status()

    # Bild löschen
    if os.path.exists(VISION_BILD):
        os.remove(VISION_BILD)

    # Wenn Personen erkannt wurden -> keine Mail
    if raum_besetzt:

        print("Raum besetzt")

        return Response("Raum besetzt", status=200)

    # Prüfen, ob der Termin schon mindestens 10 Minuten läuft
    termin_laeuft_seit = datetime.now(timezone.utc) - start_dt

    if termin_laeuft_seit.total_seconds() < 10 * 60:

        print("Raum leer, aber Termin läuft noch keine 10 Minuten")

        return Response("Termin läuft noch keine 10 Minuten", status=200)

    print("Raum leer und Termin läuft seit mindestens 10 Minuten -> Mail senden")

    title = event.get("summary", "(Kein Titel)")

    attendees = event.get("attendees", [])

    for attendee in attendees:

        email = attendee.get("email", "")

        if not email:
            continue

        if email.lower() == OWN_EMAIL.lower():
            continue

        subject = f"Raumfreigabe prüfen: {title}"

        body = f"""

Hallo,

du hast aktuell einen Raum für das Meeting {title} gebucht.In dem Raum befinden sich derzeit keine Personen.

Bitte denk dran Räume wieder frei zu geben, falls diese doch nicht benötigt werden,oder Termine verschoben werden, damit sie für andere Termine genutz werden können.

Vielen Dank!

Smart Room Warden"""

        try:

            send_email(
                gmail_service,
                email,
                subject,
                body
            )

            print(f"Mail gesendet an {email}")

        except Exception as e:

            print(e)

    return Response("Fertig", status=200)

except Exception as e:

    print(e)

    return Response("Server Fehler", status=500)

if name == "main":

app.run(
    host="0.0.0.0",
    port=5000,
ssl_context='adhoc'
)