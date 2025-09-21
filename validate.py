from ultralytics import YOLO

def validate_model():
    # Load the best model (Train5)
    model = YOLO("weights/tarin5/best.pt")
    
    # Run validation on test set
    results = model.val(
        data="dataset.yaml",  # make sure dataset.yaml has test: path defined
        split="test"          # evaluate on test set
    )
    
    # Print summary
    print("Validation results:")
    print(results)

if __name__ == "__main__":
    validate_model()
