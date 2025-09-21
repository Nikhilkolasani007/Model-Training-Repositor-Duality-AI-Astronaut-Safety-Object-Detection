from ultralytics import YOLO
import os

def run_prediction():
    # Load best model (Train5 weights)
    model = YOLO("weights/tarin5/best.pt")  
    
    # Run prediction on test images
    results = model.predict(
        source="../Hackathon2_test1/test1/images",  # path to your test images
        conf=0.25,      # confidence threshold
        save=True,      # saves predictions in runs/detect/predict
        save_txt=True,  # saves labels in YOLO format
        save_conf=True  # saves confidence scores
    )

    # Print summary
    for r in results:
        print(r.boxes)  # detected boxes

if __name__ == "__main__":
    run_prediction()
