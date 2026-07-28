import os
import sys
from typing import Any

BASE_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.dirname(BASE_DIR)
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from logger import get_logger

try:
    import cv2
except ImportError:  # pragma: no cover - optional runtime dependency
    cv2 = None

try:
    import numpy as np
except ImportError:  # pragma: no cover - optional runtime dependency
    np = None

try:
    from ultralytics import YOLO
except ImportError:  # pragma: no cover - optional runtime dependency
    YOLO = None

MODEL_PATH = os.path.join(BASE_DIR, "yolov8n.pt")

logger = get_logger(__name__)


def get_model() -> Any:
    if YOLO is None:
        raise RuntimeError("ultralytics is not installed")
    return YOLO(MODEL_PATH)


def check_raum_status(image_bytes: bytes, model: Any | None = None) -> bool:
    if np is None or cv2 is None:
        logger.error("[OKI] FEHLER: Bildverarbeitung ist nicht verfügbar")
        return False

    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if img is None:
        logger.error("[OKI] FEHLER: Bild konnte nicht dekodiert werden!")
        return False

    try:
        model_to_use = model or get_model()
        results = model_to_use(img, verbose=False)
    except Exception as exc:
        logger.error(f"[OKI] FEHLER: Modell-Analyse fehlgeschlagen: {exc}")
        return False

    people_count = 0

    for box in results[0].boxes:
        if int(box.cls[0]) == 0:
            people_count += 1

    del img
    cv2.destroyAllWindows()

    if people_count > 0:
        logger.info(f"[OKI] Ergebnis: {people_count} Person(en) gefunden!")
        return True

    logger.info("[OKI] Ergebnis: Keine Personen gefunden!")
    return False


if __name__ == "__main__":

    import argparse

    from logger import setup_logging

    setup_logging()

    parser = argparse.ArgumentParser(description="Teste die Bildanalyse mit einer Bilddatei oder dem Standardbild.")
    parser.add_argument("image", nargs="?", help="Pfad zur Testbilddatei")
    args = parser.parse_args()

    if args.image:
        with open(args.image, "rb") as f:
            image_bytes = f.read()
    else:
        sample_path = os.path.join(BASE_DIR, "room.jpg")
        if not os.path.exists(sample_path):
            logger.error("[OKI] FEHLER: Kein Testbild gefunden und kein Pfad angegeben.")
            raise SystemExit(1)
        with open(sample_path, "rb") as f:
            image_bytes = f.read()

    logger.info("Starte KI-Testlauf...")

    result = check_raum_status(image_bytes)

    logger.info(f"Raum besetzt: {result}")
