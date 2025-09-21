from ultralytics import YOLO

def train_model():
    # Load YOLOv8 small model
    model = YOLO("yolov8s.pt")  
    
    # Train on your dataset
    results = model.train(
        data="dataset.yaml",  # path to dataset.yaml
        epochs=60,            # we used 60 for Train5
        imgsz=640,
        batch=16,
        device=0              # GPU
    )
    return results

if __name__ == "__main__":
    train_model()
