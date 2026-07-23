import cv2
import numpy as np
import os
from ultralytics import YOLO

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "yolov8n.pt")

# KI-Modell laden
model = YOLO(MODEL_PATH)


def check_raum_status(image_bytes):

    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if img is None:
        print("[OKI] FEHLER: Bild konnte nicht dekodiert werden!")
        return False

    results = model(img, verbose=False)

    people_count = 0

    for box in results[0].boxes:
        if int(box.cls[0]) == 0:
            people_count += 1

    del img
    cv2.destroyAllWindows()

    if people_count > 0:
        print(f"[OKI] Ergebnis: {people_count} Person(en) gefunden!")
        return True

    else:
        print("[OKI] Ergebnis: Keine Personen gefunden!")
        return False


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description="Teste die Bildanalyse mit einer Bilddatei oder dem Standardbild.")
    parser.add_argument("image", nargs="?", help="Pfad zur Testbilddatei")
    args = parser.parse_args()

    if args.image:
        with open(args.image, "rb") as f:
            image_bytes = f.read()
    else:
        sample_path = os.path.join(BASE_DIR, "room.jpg")
        if not os.path.exists(sample_path):
            print("[OKI] FEHLER: Kein Testbild gefunden und kein Pfad angegeben.")
            raise SystemExit(1)
        with open(sample_path, "rb") as f:
            image_bytes = f.read()

    print("Starte KI-Testlauf...")

    result = check_raum_status(image_bytes)

    print("Raum besetzt:", result)
