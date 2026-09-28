# 🌿 Plant Disease Classifier (PlantGuard AI)

An AI-powered agricultural web application built with **Streamlit** and **TensorFlow / Keras (ResNet-50)** to diagnose plant leaf diseases from photographs, analyze symptoms, and provide actionable remedies and treatment advice.

---

## 🌟 Key Features

- **Deep Learning Diagnosis:** Powered by a transfer-learned **ResNet-50** model trained on the PlantVillage dataset covering **38 distinct classes** across 14 crop types.
- **Multiple Input Modes:**
  - 📁 **File Upload:** Upload any `.jpg`, `.jpeg`, or `.png` leaf photo.
  - 📷 **Live Camera Capture:** Snap a picture directly with your webcam or mobile camera.
  - 🧪 **Preloaded Sample Images:** Instantly test healthy leaves, rust-spotted leaves, and blight lesions without needing downloads.
- **Comprehensive Disease Advisory:**
  - 🟢 **Healthy Confirmation** vs 🔴 **Disease Detection** badges.
  - Detailed overview and underlying pathogen causes.
  - Characteristic visual symptoms to check for on foliage.
  - Recommended **organic and chemical treatments / remedies**.
  - **Preventive agricultural practices** (irrigation, crop rotation, sanitization).
- **Probabilities & Technical Metrics:** Top-5 probability breakdown with visual confidence meters and inference metadata.
- **Interactive Crop Catalog:** Explore all 38 supported crop-disease combinations right from the sidebar.

---

## 🚀 How to Run the App

### Option 1: Double-Click (Easiest for Windows)
Simply double-click `run_app.bat` in this folder. It will verify dependencies and open the app in your browser automatically!

### Option 2: Terminal / PowerShell Command
1. Open PowerShell or Command Prompt in this project folder:
   ```bash
   cd c:\Users\T490\Downloads\plant-disease-app
   ```
2. Install dependencies (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Streamlit will launch your browser at `http://localhost:8501`.

---

## 📂 Project Structure

```text
plant-disease-app/
├── app.py                                # Main Streamlit web application
├── disease_info.py                       # Disease knowledge base (symptoms, treatments, prevention)
├── class_names.json                      # 38 PlantVillage class labels
├── requirements.txt                      # Python dependencies
├── run_app.bat                           # 1-click Windows batch launcher
├── run_app.ps1                           # PowerShell launcher script
├── resnet50_plant_disease_final.keras    # Trained ResNet-50 weights
├── sample_images/                        # Sample leaf images for quick testing
└── README.md                             # Documentation & guide
```

---

## 🌾 Supported Crops & Conditions (38 Classes)

- **Apple:** Scab, Black rot, Cedar apple rust, Healthy
- **Blueberry:** Healthy
- **Cherry:** Powdery mildew, Healthy
- **Corn (Maize):** Cercospora leaf spot (Gray leaf spot), Common rust, Northern leaf blight, Healthy
- **Grape:** Black rot, Esca (Black measles), Leaf blight (Isariopsis spot), Healthy
- **Orange:** Huanglongbing (Citrus greening)
- **Peach:** Bacterial spot, Healthy
- **Pepper (Bell):** Bacterial spot, Healthy
- **Potato:** Early blight, Late blight, Healthy
- **Raspberry:** Healthy
- **Soybean:** Healthy
- **Squash:** Powdery mildew
- **Strawberry:** Leaf scorch, Healthy
- **Tomato:** Bacterial spot, Early blight, Late blight, Leaf mold, Septoria leaf spot, Spider mites, Target spot, Yellow leaf curl virus, Mosaic virus, Healthy
