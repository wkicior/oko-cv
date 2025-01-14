from ultralytics import YOLO

#model = YOLO("yolo11n.pt")
model = YOLO("./runs/detect/train2/weights/last.pt")
results = model.train(data="../datasets/Alaina_CNN/data.yaml", epochs=50, imgsz=320, device="mps", resume=True)
