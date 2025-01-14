import cv2
import cvzone
from ultralytics import YOLO
import math

#model = YOLO("yolo11n.pt")

model = YOLO("./runs/detect/train2/weights/last.pt")
print(f"Available model names: {model.names}")

def show_box(box):
    x1, y1, x2, y2 = box.xyxy[0]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    w, h = x2 - x1, y2 - y1
    confidentiality = math.ceil((box.conf[0] * 100)) / 10
    name = model.names[int(box.cls[0])]
    cvzone.cornerRect(frame, (x1, y1, w, h))
    cvzone.putTextRect(frame, f"{name} {confidentiality}", (max(0, x1), max(35, y1)), scale = 1.0)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        results = model(frame, stream=True, verbose=False)
        for r in results:
            for box in r.boxes:
                show_box(box)
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
