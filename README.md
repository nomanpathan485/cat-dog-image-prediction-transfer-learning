<div align="center">

# 🐱 Cat vs 🐶 Dog Image Classifier

### A side-by-side study of **training a CNN from scratch vs. fine-tuning MobileNetV2** — culminating in a Flask web app that classifies uploaded images with **~96.5% validation accuracy**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" alt="Keras"/>
  <img src="https://img.shields.io/badge/MobileNetV2-Transfer%20Learning-00BFFF?style=for-the-badge" alt="MobileNetV2"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/Accuracy-96.5%25-success?style=for-the-badge" alt="Accuracy"/>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/nomanpathan485/cat-dog-image-prediction-transfer-learning?style=social" alt="Stars"/>
  <img src="https://img.shields.io/github/forks/nomanpathan485/cat-dog-image-prediction-transfer-learning?style=social" alt="Forks"/>
  <img src="https://img.shields.io/github/watchers/nomanpathan485/cat-dog-image-prediction-transfer-learning?style=social" alt="Watchers"/>
</p>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-key-result">Key Result</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-roadmap">Roadmap</a> •
  <a href="#-author">Author</a>
</p>

</div>

---

## 🔍 Overview

This project answers a deceptively simple question:

> *"When should I fine-tune a pretrained model instead of training my own CNN from scratch?"*

I built **two** models on the same Cat vs Dog dataset and compared them honestly:

| Approach                      | Validation Accuracy | Notes                                  |
|-------------------------------|---------------------|----------------------------------------|
| 🐣 CNN **from scratch**       | **~76 %**           | Unstable on new images                 |
| 🚀 **MobileNetV2** fine-tuned | **~96.5 %**         | +20 pts, much more robust              |

The fine-tuned MobileNetV2 is then wrapped in a tiny **Flask** web app — upload an image, get an instant prediction with confidence.

---

## 📸 Demo

<div align="center">

### Web App UI

<img src="screenshot/Screenshot 2026-06-08 183737.png" alt="Cat vs Dog Classifier UI" width="600"/>

### Live Demo Recording

[▶️ Watch the screen recording](screenshot/Screen%20Recording%202026-06-08%20200750.mp4)

</div>

> 📌 *Replace these with cleaner screenshots after running the app locally.*

---

## 🏆 Key Result

| Metric                 | CNN from scratch | MobileNetV2 (fine-tuned) |
|------------------------|------------------|---------------------------|
| **Validation accuracy**| ~76 %            | **~96.5 %** ✅            |
| Generalization         | Poor on new data | Strong                    |
| Training time          | ~20 min (GPU)    | ~5 min (GPU)              |
| Model size             | ~80 MB           | ~9 MB                     |
| Best use case          | Learning CNNs    | Real deployment ✅        |

**Takeaway:** Pretrained backbones capture universal visual features (edges → textures → objects). Fine-tuning a tiny classification head on top almost always beats training from scratch — especially on small datasets.

---

## ✨ Features

- 🔬 **Two-model comparison** (CNN-from-scratch vs MobileNetV2)
- 🧠 **Transfer learning** with selective layer unfreezing (last 20 layers trainable)
- 📐 **GlobalAveragePooling2D** instead of Flatten — fewer params, less overfitting
- 🌐 **Flask web UI** — drag-drop, click Predict, see result
- 🎚️ **Confidence score** shown with every prediction
- 💾 **Saved Keras model** — no need to retrain

---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white" alt="Keras"/>
  <img src="https://img.shields.io/badge/MobileNetV2-00BFFF?style=flat-square" alt="MobileNetV2"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Pillow-EE5A24?style=flat-square" alt="Pillow"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML"/>
</p>

| Layer              | Tool                                   |
|--------------------|----------------------------------------|
| Language           | Python 3.8+                            |
| Deep Learning      | TensorFlow 2.x / Keras                 |
| Pretrained Backbone| MobileNetV2 (ImageNet weights)         |
| Pooling Head       | `GlobalAveragePooling2D`               |
| Classifier Head    | `Dense(128, ReLU)` → `Dense(1, sigmoid)`|
| Web Framework      | Flask                                  |
| Frontend           | HTML + minimal CSS                     |
| Image Preprocessing| Pillow + Keras image utils             |

---

## 📂 Project Structure

```
cat-dog-transfer-learning/
│
├── 🐍 train.py              # Builds & fine-tunes the MobileNetV2 model
├── 🐍 predict.py            # Standalone inference on a single image
├── 🐍 app.py                # Flask web server (UI + /predict endpoint)
├── 🧠 cat_dog_transfer_model.keras   # Trained model weights
├── 📄 README.md             # You are here
├── 📦 requirements.txt      # Python dependencies
│
├── 📁 templates/
│   └── 🌐 index.html        # Upload form + result panel
│
└── 📁 screenshot/
    ├── 🖼️ Screenshot 2026-06-08 183737.png
    └── 🎥 Screen Recording 2026-06-08 200750.mp4
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/nomanpathan485/cat-dog-image-prediction-transfer-learning.git
cd cat-dog-image-prediction-transfer-learning
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

> 💡 TensorFlow pulls in a ~500 MB install. If you're on a CPU-only machine, expect training to be slow.

---

## 🚀 Usage

### A) Train the model (optional — already trained weights included)

```bash
python train.py
```

- Loads the **Cat vs Dog** dataset from `cat-dog-image-classifier-cnn/dataset/PetImages`
- Fine-tunes MobileNetV2 (ImageNet weights) for **3 epochs**
- Saves the trained model to `cat_dog_transfer_model.keras`

### B) Run the web app

```bash
python app.py
```

Then open **http://127.0.0.1:5000** in your browser:

1. Click **Choose File** → pick any cat or dog image
2. Click **Predict**
3. See the prediction + confidence score

### C) Predict from the command line

```bash
python predict.py
```

*(Or import `predict.py`'s logic into your own script — it wraps the same Keras model.)*

---

## 🧠 Architecture

<div align="center">

```
Input Image (128 × 128 × 3)
        ↓
┌────────────────────────────┐
│   MobileNetV2 Backbone     │  ← ImageNet weights
│   (last 20 layers trainable)│
└────────────────────────────┘
        ↓
┌────────────────────────────┐
│ GlobalAveragePooling2D     │  ← fewer params than Flatten
└────────────────────────────┘
        ↓
┌────────────────────────────┐
│ Dense(128, ReLU)           │  ← classification head
└────────────────────────────┘
        ↓
┌────────────────────────────┐
│ Dense(1, Sigmoid)          │  ← P(dog)
└────────────────────────────┘
        ↓
   Prediction + Confidence
```

</div>

**Why these choices?**

- **`MobileNetV2`** — lightweight (~9 MB), perfect for CPU-friendly deployment
- **Fine-tune only the last 20 layers** — preserves low-level features learned on ImageNet
- **`GlobalAveragePooling2D`** — drastically reduces parameters vs `Flatten()`, fighting overfitting
- **Low learning rate (`1e-5`)** — protects pretrained weights from catastrophic forgetting

---

## 🧠 What I Learned

- ✅ CNNs from scratch are valuable for learning but **underperform** on real, limited data
- ✅ **Transfer learning** beats from-scratch training by +20 pts on the same dataset
- ✅ **MobileNetV2** is small enough to deploy yet still very accurate
- ✅ **`GlobalAveragePooling2D`** reduces parameters and overfitting vs `Flatten`
- ✅ **Selective layer unfreezing** lets you fine-tune efficiently without losing pretrained knowledge
- ✅ Small architecture choices (pooling type, head depth, LR) compound into big accuracy differences

---

## 🗺️ Roadmap

- [ ] 🖼️ Add a CNN-from-scratch training script for the side-by-side comparison
- [ ] 📊 Plot training/validation accuracy & loss curves
- [ ] 🔍 Add Grad-CAM visualization to interpret what the model sees
- [ ] 🎨 Improve the web UI — drag-and-drop, progress bar, error handling
- [ ] 🐳 Dockerize the Flask app for one-command deployment
- [ ] ☁️ Deploy to Render / Railway / Hugging Face Spaces
- [ ] 📦 Add model quantization (TFLite) for mobile inference
- [ ] 🧪 Add a small test set evaluation script with a confusion matrix

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- 🐶🐱 Dataset: [Microsoft Cats vs Dogs](https://www.microsoft.com/en-us/download/details.aspx?id=54765) (via Kaggle's PetImages)
- 🧠 Pretrained backbone: [MobileNetV2](https://arxiv.org/abs/1801.04381) — Sandler et al., 2018
- 📚 Andrew Ng's Deep Learning course — inspiration for the transfer-learning workflow

---

## 👤 Author

**Noaman Ayub Pathan** — AI & Data Science Student

<p>
  <a href="https://github.com/nomanpathan485"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://www.linkedin.com/in/noaman-ayub-pathan/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
</p>

<p align="left">
  <img src="https://komarev.com/ghpvc/?username=nomanpathan485&label=Profile%20views&color=0e75b6&style=flat" alt="Profile views"/>
</p>

---

<div align="center">

### ⭐ If you found this useful, drop a star — it helps a lot!

</div>
