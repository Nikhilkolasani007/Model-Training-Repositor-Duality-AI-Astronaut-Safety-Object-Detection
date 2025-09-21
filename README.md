# 🚀 Duality AI Hackathon – Object Detection with YOLOv8

This repository contains our solution for the **Hack With Hyderabad – Duality Problem Statement**.  
We trained a **YOLOv8 model** to detect **7 critical safety objects** inside a space-station environment.  
Additionally, we built a **mini full-stack application** (Frontend + Backend + PocketBase) to deploy the model.

---

## 📂 Repository Structure

```
├── dataset.yaml              # Dataset configuration (update paths!)
├── train.py                  # Script to train the YOLOv8 model
├── predict.py                # Script to run inference on test images
├── test.py                   # Script to evaluate model on test dataset
├── weights/
│   └── best.pt               # Trained model weights (from Train5, 60 epochs)
├── runs/                     # YOLOv8 outputs (sample only, full in GDrive)
├── README.md                 # Documentation
```

---

## 🔧 Setup Instructions

1. **Clone Repository**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Install Dependencies**
   ```bash
   pip install ultralytics
   ```

3. **Dataset Setup**
   - Your dataset should follow YOLO format:
     ```
     dataset/
     ├── train/
     │   ├── images/
     │   └── labels/
     ├── val/
     │   ├── images/
     │   └── labels/
     ├── test/
     │   ├── images/
     │   └── labels/
     ```
   - Update `dataset.yaml` with your **absolute or relative paths**, for example:
     ```yaml
     path: ../Hackathon2_train1/train_1   # <-- update this
     train: train1/images
     val: val1/images
     test: test1/images

     nc: 7
     names: [ 'OxygenTank', 'NitrogenTank', 'FirstAidBox', 'FireAlarm',
              'SafetySwitchPanel', 'EmergencyPhone', 'FireExtinguisher' ]
     ```

---

## 🏋️ Training

To train from scratch (we trained up to **60 epochs**):

```bash
python train.py
```

or via CLI:

```bash
yolo detect train model=yolov8s.pt data=dataset.yaml epochs=60 imgsz=640 batch=16
```

- Best weights saved at:
  ```
  runs/detect/train5/weights/best.pt
  ```

---

## 🔮 Prediction (Inference)

Run predictions on test images:

```bash
python predict.py
```

By default, it looks in:
```
../Hackathon2_test1/test1/images
```

👉 **Update path in `predict.py`** if your test folder is different:
```python
results = model.predict(
    source="../Hackathon2_test1/test1/images",  # <-- change this path
    conf=0.25,
    save=True,
    save_txt=True,
    save_conf=True
)
```

Results will be saved in:
```
runs/predict/predict1/
```

---

## 📊 Evaluation (Testing)

Run evaluation on your test set:

```bash
python test.py
```

This uses:
```python
results = model.val(
    data="dataset.yaml",  # <-- make sure dataset.yaml has test path
    split="test"
)
```

It will output **Precision, Recall, mAP50, mAP50-95**.

---

## 📈 Final Scores (Train5, 60 Epochs)

- **Precision:** 0.919  
- **Recall:** 0.727  
- **mAP@0.5:** 0.800  
- **mAP@0.5:0.95:** 0.668  

---

## 📂 Additional Resources

- **Google Drive (Full dataset + runs + large files):** [Insert Link Here]  
- **Model Repo (this one):** [Insert GitHub Link]  
- **Application Repo:** [Insert Link Here]  
- **PPT (Hackathon Slides):** [Insert Link Here]  
- **Hackathon Report (PDF/DOCX):** [Insert Link Here]  

---

## ⚡ Notes
- Keep repo size small → only include **weights/best.pt**, scripts, and configs.  
- Full runs + raw dataset (~12GB) should go in **Google Drive**.  
- This README will guide both judges and developers to reproduce results.

---

## 🙌 Team
**Team 404 NOT FOUND** – Hack With Hyderabad  
