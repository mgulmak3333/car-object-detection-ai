# Voren-X1 | Car Object Detection AI 🚗

<p align="left">
  <img src="https://raw.githubusercontent.com/mgulmak3333/car-object-detection-ai/refs/heads/main/tittle.png" alt="Brain MRI Scans" width="500">
</p>

<p align="left">
  <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" alt="TensorFlow">
  <img src="https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <a href="https://www.kaggle.com/musaglmak" target="_blank">
    <img src="https://img.shields.io/badge/Kaggle-%2320BEFF.svg?style=for-the-badge&logo=Kaggle&logoColor=white" alt="Kaggle">
  </a>
</p>

---
## Kaggle Profile: https://www.kaggle.com/musaglmak

## Kaggle Voren-X1 Model: https://www.kaggle.com/models/musaglmak/voren
---

## 🚀 Model Links & Live Demo

* **Demo Link:** https://car-object-detection-ai-ludx7efpumrswidwi8tev9.streamlit.app/
* **Trained Model & Documentation:** You can access the trained model weights (`voren.pt`) and the model card on Kaggle via [voren on Kaggle](https://www.kaggle.com/models/musaglmak/voren).

---

## 📊 Dataset & Classes

The model is fine-tuned to detect a single, specific class in images:
1. **Car** (Automobiles/Vehicles)

The dataset used for training is 100% custom-curated, consisting of hand-labeled images focused solely on vehicle identification.

---

## 🛠️ Tech Stack & Dependencies
* **Deep Learning Framework:** PyTorch (Ultralytics)
* **Model Architecture:** YOLOv26n (Fine-Tuning)
* **Model Complexity:** 2,504,190 Total Parameters (Highly optimized and lightweight for fast CPU/edge inference)
* **Web Interface:** Streamlit
* **Data Processing & Computer Vision:** NumPy, Pillow (PIL), OpenCV-Python

---

## 💻 Installation & Local Setup

Follow these steps to run the Streamlit application on your local machine:

### 1. Clone the Repository
```bash
https://github.com/mgulmak3333/car-object-detection-ai
cd car-object-detection-ai

```

### 2. Install Requirements

Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt

```

### 3. Download the Model

Download the `voren.pt` file from the Kaggle link provided above and place it into the root directory of this project.

### 4. Run the Streamlit App

```bash
streamlit run app.py

```

---

## 📜 License & Copyright

Copyright © 2026 [mgulmak3333](https://github.com/mgulmak3333).  
This project is licensed under the **Apache License 2.0**. 

You are free to use, modify, and distribute this software under the terms of the Apache 2.0 License. For more details, please see the [LICENSE](LICENSE) file in the repository.
