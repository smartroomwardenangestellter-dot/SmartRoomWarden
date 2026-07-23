import cv2
import os
from ultralytics import YOLO

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "yolov8n.pt")

# KI-Modell laden
model = YOLO(MODEL_PATH)


def check_raum_status():

    bild_pfad = os.path.join(BASE_DIR, "room.jpg")

    print(f"\n[OKI] Analysiere Bild: {bild_pfad} ...")

    if not os.path.exists(bild_pfad):
        print(f"[OKI] FEHLER: Bild '{bild_pfad}' nicht gefunden!")
        return False

    img = cv2.imread(bild_pfad)

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

    print("Starte KI-Testlauf...")

    result = check_raum_status()

    print("Raum besetzt:", result)
