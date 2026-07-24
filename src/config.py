import os
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SRC_DIR.parent
KI_DIR = SRC_DIR / "ki_zeugs"
LOG_DIR = PROJECT_ROOT / "logs"
RUNTIME_MODE = os.getenv("SMARTROOMWARDEN_RUNTIME_MODE") or "simulation"


def _read_dotenv_lines(dotenv_path: Path) -> dict[str, str]:
    values: dict[str, str] = {}

    if not dotenv_path.exists():
        return values

    for raw_line in dotenv_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            values[key] = value

    return values


def _load_dotenv() -> None:
    base_values = _read_dotenv_lines(PROJECT_ROOT / ".env")
    mode_values = _read_dotenv_lines(PROJECT_ROOT / f".env.{RUNTIME_MODE}")

    for key, value in base_values.items():
        os.environ.setdefault(key, value)

    for key, value in mode_values.items():
        if key in os.environ and os.environ.get(key) == base_values.get(key):
            os.environ[key] = value
        else:
            os.environ.setdefault(key, value)


_load_dotenv()


def _resolve_path(value: str | None, default: Path) -> Path:
    if not value:
        return default

    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = (PROJECT_ROOT / candidate).resolve()
    return candidate.resolve()


GOOGLE_CREDENTIALS_PATH = _resolve_path(
    os.getenv("GOOGLE_CREDENTIALS_PATH"),
    PROJECT_ROOT / "credentials.json",
)
GOOGLE_TOKEN_PATH = _resolve_path(
    os.getenv("GOOGLE_TOKEN_PATH"),
    PROJECT_ROOT / "token.json",
)
DEVICE_TOKEN = os.getenv("SMARTROOMWARDEN_DEVICE_TOKEN") or os.getenv("DEVICE_TOKEN") or "PiChallenge_2026"
OWN_EMAIL = os.getenv("SMARTROOMWARDEN_OWN_EMAIL") or os.getenv("OWN_EMAIL") or "smartroomwarden@gmail.com"

VISION_BILD = KI_DIR / "room.jpg"
MODEL_PATH = KI_DIR / "yolov8n.pt"
