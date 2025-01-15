from ultralytics import YOLO

# first run
model = YOLO("yolo11n.pt")
results = model.train(data="../datasets/Alaina_CNN/data.yaml", epochs=50, imgsz=320, device="mps")

# resume if needed
#model = YOLO("./runs/detect/train/weights/last.pt")
#results = model.train(data="../datasets/Alaina_CNN/data.yaml", epochs=50, imgsz=320, device="mps", resume=True)
