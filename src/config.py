import os
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent
KI_DIR = SRC_DIR / "ki_zeugs"
LOG_DIR = SRC_DIR.parent / "logs"

GOOGLE_CREDENTIALS_PATH = Path(os.getenv("GOOGLE_CREDENTIALS_PATH", SRC_DIR / "credentials.json"))
GOOGLE_TOKEN_PATH = Path(os.getenv("GOOGLE_TOKEN_PATH", SRC_DIR / "token.json"))
DEVICE_TOKEN = os.getenv("SMARTROOMWARDEN_DEVICE_TOKEN", "***REMOVED-DEVICE-TOKEN***")
OWN_EMAIL = os.getenv("SMARTROOMWARDEN_OWN_EMAIL", "removed-email@example.invalid")

VISION_BILD = KI_DIR / "room.jpg"
MODEL_PATH = KI_DIR / "yolov8n.pt"
