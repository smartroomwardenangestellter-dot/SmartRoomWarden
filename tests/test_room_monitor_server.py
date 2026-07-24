import importlib.util
import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from unittest.mock import Mock


def load_room_monitor_module() -> Any:
    project_root = Path(__file__).resolve().parents[1]
    module_path = project_root / "src" / "api&flask" / "room_monitor_server.py"
    spec = importlib.util.spec_from_file_location("room_monitor_server", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {module_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules["room_monitor_server"] = module
    spec.loader.exec_module(module)
    return module


room_monitor_server = load_room_monitor_module()


class RoomMonitorServerTests(unittest.TestCase):
    module: Any

    @classmethod
    def setUpClass(cls):
        cls.module = room_monitor_server
        cls.module.app.testing = True
        cls.client = cls.module.app.test_client()
        cls.valid_headers = {"X-Device-Token": cls.module.DEVICE_TOKEN}

    def test_status_unauthorized_without_token(self):
        response = self.client.get("/status")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data.decode(), "unauthorized")

    def test_status_returns_true_when_event_active(self):
        self.module.get_services = Mock(return_value=(Mock(), Mock()))
        self.module.get_current_event = Mock(return_value=("event", datetime.now(timezone.utc)))

        response = self.client.get("/status", headers=self.valid_headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "true")

    def test_status_returns_false_when_no_event(self):
        self.module.get_services = Mock(return_value=(Mock(), Mock()))
        self.module.get_current_event = Mock(return_value=(None, None))

        response = self.client.get("/status", headers=self.valid_headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "false")

    def test_status_returns_service_unavailable_when_google_service_init_fails(self):
        self.module.get_services = Mock(side_effect=RuntimeError("boom"))

        response = self.client.get("/status", headers=self.valid_headers)

        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.data.decode(), "Dienst nicht verfügbar")

    def test_validate_configuration_reports_missing_credentials(self):
        self.module.GOOGLE_CREDENTIALS_PATH = Path("missing-creds.json")
        self.module.GOOGLE_TOKEN_PATH = Path("token.json")
        self.module.DEVICE_TOKEN = "test-token"
        self.module.OWN_EMAIL = "owner@example.com"

        issues = self.module.validate_configuration()

        self.assertIn("Google credentials file not found", issues[0])

    def test_upload_sends_email_when_room_empty_and_event_running_long_enough(self):
        self.module.get_services = Mock(return_value=(Mock(), Mock()))
        self.module.get_current_event = Mock(
            return_value=(
                {
                    "summary": "Team Meeting",
                    "attendees": [{"email": "guest@example.com"}, {"email": self.module.OWN_EMAIL}],
                },
                datetime.now(timezone.utc) - timedelta(minutes=11),
            )
        )
        self.module.check_raum_status = Mock(return_value=False)
        self.module.send_email = Mock()

        response = self.client.post(
            "/upload",
            headers=self.valid_headers,
            data=b"fake-image-bytes",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("Fertig", response.data.decode())
        self.module.send_email.assert_called_once()

    def test_upload_returns_room_occupied_when_person_detected(self):
        self.module.get_services = Mock(return_value=(Mock(), Mock()))
        self.module.get_current_event = Mock(
            return_value=(
                {"summary": "Team Meeting"},
                datetime.now(timezone.utc) - timedelta(minutes=20),
            )
        )
        self.module.check_raum_status = Mock(return_value=True)

        response = self.client.post(
            "/upload",
            headers=self.valid_headers,
            data=b"fake-image-bytes",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Raum besetzt")

    def test_upload_returns_no_active_event(self):
        self.module.get_services = Mock(return_value=(Mock(), Mock()))
        self.module.get_current_event = Mock(return_value=(None, None))

        response = self.client.post(
            "/upload",
            headers=self.valid_headers,
            data=b"fake-image-bytes",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Kein aktiver Termin")

    def test_upload_returns_bad_request_for_missing_image(self):
        self.module.get_services = Mock(return_value=(Mock(), Mock()))
        self.module.get_current_event = Mock(
            return_value=(
                {"summary": "Team Meeting"},
                datetime.now(timezone.utc) - timedelta(minutes=20),
            )
        )

        response = self.client.post(
            "/upload",
            headers=self.valid_headers,
            data=b"",
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), "Kein Bild")


if __name__ == "__main__":
    unittest.main()
