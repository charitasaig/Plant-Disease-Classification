import json
import os
import sys
from pathlib import Path
from typing import List, Tuple, Optional

# Suppress verbose TensorFlow C++ logging
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import numpy as np
from PIL import Image
import streamlit as st

# Setup search paths
APP_DIR = Path(__file__).resolve().parent
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))
if str(APP_DIR.parent) not in sys.path:
    sys.path.insert(0, str(APP_DIR.parent))

try:
    from disease_info import get_disease_info, DISEASE_DATA
except ImportError:
    def get_disease_info(raw: str):
        is_healthy = "healthy" in raw.lower()
        return {
            "status": "Healthy" if is_healthy else "Diseased",
            "description": "Plant health condition identified by model.",
            "symptoms": "Normal growth" if is_healthy else "Foliar spots or lesions detected.",
            "causes": "Environmental factors.",
            "treatment": "No treatment required." if is_healthy else "Isolate and apply recommended fungicides/bactericides.",
            "prevention": "Ensure good drainage, air circulation, and sanitize equipment."
        }
    DISEASE_DATA = {}

# Page configuration
st.set_page_config(
    page_title="PlantGuard AI | Leaf Disease Classifier",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1b5e20;
        margin-bottom: 0.1rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #444;
        margin-bottom: 1.2rem;
    }
    .badge-healthy {
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 1.05rem;
        display: inline-block;
        border: 1px solid #a5d6a7;
    }
    .badge-diseased {
        background-color: #ffebee;
        color: #c62828;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 1.05rem;
        display: inline-block;
        border: 1px solid #ef9a9a;
    }
    .section-header {
        font-size: 1.15rem;
        font-weight: 600;
        color: #2e7d32;
        margin-top: 15px;
        margin-bottom: 6px;
    }
</style>
""", unsafe_allow_html=True)

IMG_SIZE = 224


def resolve_file_path(filename: str) -> Optional[Path]:
    """Search multiple locations for a required file."""
    candidates = [
        APP_DIR / filename,
        APP_DIR / "plant-disease-app" / filename,
        APP_DIR.parent / filename,
        APP_DIR.parent / "plant-disease-app" / filename,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    return None


MODEL_PATH = resolve_file_path("resnet50_plant_disease_final.keras")
CLASS_NAMES_PATH = resolve_file_path("class_names.json")


@st.cache_resource(show_spinner="⏳ Loading trained ResNet-50 weights (cached after 1st run)...")
def get_model():
    """Load and cache the trained Keras model lazily on demand."""
    if MODEL_PATH is None or not MODEL_PATH.exists():
        return None
    from tensorflow.keras.models import load_model
    return load_model(MODEL_PATH)


@st.cache_resource
def load_class_names() -> List[str]:
    """Load and cache class names JSON."""
    if CLASS_NAMES_PATH is None or not CLASS_NAMES_PATH.exists():
        return []
    with CLASS_NAMES_PATH.open(encoding="utf-8") as f:
        names = json.load(f)
    return names


def preprocess_leaf(image: Image.Image):
    """Prepare PIL image for ResNet50 inference."""
    import tensorflow as tf
    from tensorflow.keras.applications.resnet50 import preprocess_input

    img = image.convert("RGB")
    img_array = np.array(img).astype(np.float32)
    img_tensor = tf.convert_to_tensor(img_array)
    img_tensor = tf.image.resize(img_tensor, (IMG_SIZE, IMG_SIZE))
    img_tensor = tf.expand_dims(img_tensor, axis=0)
    return preprocess_input(img_tensor)


def predict_leaf(model, image: Image.Image, class_names: List[str]) -> List[Tuple[str, float]]:
    """Predict top 5 classes and their percentage probabilities."""
    processed = preprocess_leaf(image)
    probs = model.predict(processed, verbose=0)[0]
    top5_indices = np.argsort(probs)[-5:][::-1]
    return [(class_names[i], float(probs[i] * 100.0)) for i in top5_indices]


def format_label(raw: str) -> Tuple[str, str]:
    """Extract clean Crop Name and Disease Condition."""
    if "___" in raw:
        crop_part, disease_part = raw.split("___", 1)
        crop = crop_part.replace("_", " ").strip()
        disease = disease_part.replace("_", " ").strip()
        return crop, disease
    return raw.replace("_", " ").strip(), ""


# ==========================================
# Sidebar
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/natural-food.png", width=70)
    st.title("PlantGuard AI")
    st.caption("AI-Powered Crop Health Diagnosis")
    st.divider()

    st.subheader("📌 Model Specs")
    st.markdown("""
    - **Backbone:** ResNet-50 CNN
    - **Dataset:** PlantVillage (38 Classes)
    - **Input Resolution:** 224 × 224 px
    """)

    st.divider()

    st.subheader("💡 Photo Taking Tips")
    st.markdown("""
    - **Fill Frame:** Center a single leaf in the photo.
    - **Good Light:** Use diffused natural daylight.
    - **Clear Focus:** Ensure lesions or spots are sharp and in focus.
    """)

    st.divider()

    class_names = load_class_names()
    with st.expander(f"🌿 38 Supported Conditions"):
        crops = {}
        for c in class_names:
            crop, dis = format_label(c)
            crops.setdefault(crop, []).append(dis if dis else "Healthy")
        
        for crop, diseases in sorted(crops.items()):
            st.markdown(f"**{crop}** ({len(diseases)})")
            for d in diseases:
                st.caption(f"• {d}")


# ==========================================
# Main Content Area
# ==========================================
st.markdown('<div class="main-title">🌿 Plant Disease Classifier</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Identify plant leaf diseases using deep learning, with symptoms analysis and treatment advice.</div>',
    unsafe_allow_html=True
)

if MODEL_PATH is None or not MODEL_PATH.exists():
    st.error("⚠️ Trained model file `resnet50_plant_disease_final.keras` was not found.")
    st.info(f"Please ensure `resnet50_plant_disease_final.keras` is in `{APP_DIR}`.")
    st.stop()

if not class_names:
    st.error("⚠️ `class_names.json` could not be loaded.")
    st.stop()

# Input Mode Selection
input_mode = st.radio(
    "Choose Image Input Method:",
    ("📁 Upload Leaf Image", "🧪 Try Sample Leaves", "📷 Take Photo with Camera"),
    horizontal=True
)

selected_image: Optional[Image.Image] = None
image_source_label = ""

col_input, col_preview = st.columns([1.1, 0.9])

with col_input:
    if input_mode == "📁 Upload Leaf Image":
        uploaded_file = st.file_uploader(
            "Upload a leaf photograph (JPG, JPEG, PNG):",
            type=["jpg", "jpeg", "png"],
            help="Select a clear photo of an individual leaf"
        )
        if uploaded_file is not None:
            try:
                selected_image = Image.open(uploaded_file)
                image_source_label = f"Uploaded File: {uploaded_file.name}"
            except Exception as e:
                st.error(f"Error opening image: {e}")

    elif input_mode == "🧪 Try Sample Leaves":
        sample_options = {
            "Sample 1: Healthy Green Leaf": "sample_healthy_leaf.jpg",
            "Sample 2: Leaf with Rust Spots": "sample_rust_spots.jpg",
            "Sample 3: Leaf with Blight Lesions": "sample_blight_lesions.jpg"
        }
        chosen_sample_name = st.selectbox("Select a pre-loaded sample:", list(sample_options.keys()))
        sample_filename = sample_options[chosen_sample_name]
        sample_path = resolve_file_path(f"sample_images/{sample_filename}")
        
        if sample_path and sample_path.exists():
            selected_image = Image.open(sample_path)
            image_source_label = f"{chosen_sample_name}"
        else:
            st.warning("Sample image not found on disk.")

    elif input_mode == "📷 Take Photo with Camera":
        camera_pic = st.camera_input("Snap a photo of the plant leaf:")
        if camera_pic is not None:
            try:
                selected_image = Image.open(camera_pic)
                image_source_label = "Camera Snapshot"
            except Exception as e:
                st.error(f"Error reading camera photo: {e}")

with col_preview:
    if selected_image is not None:
        try:
            st.image(selected_image, caption=image_source_label, width="stretch")
        except TypeError:
            st.image(selected_image, caption=image_source_label, use_container_width=True)
        w, h = selected_image.size
        st.caption(f"Image Resolution: {w} × {h} px | Mode: {selected_image.mode}")
    else:
        st.info("👈 Please select or upload a leaf image to proceed.")

# ==========================================
# Prediction & Advisory Section
# ==========================================
if selected_image is not None:
    st.divider()
    
    predict_col, _ = st.columns([1.5, 3.5])
    with predict_col:
        try:
            run_prediction = st.button("🔍 Diagnose Leaf Health", type="primary", width="stretch")
        except TypeError:
            run_prediction = st.button("🔍 Diagnose Leaf Health", type="primary", use_container_width=True)

    if run_prediction:
        with st.spinner("Analyzing leaf with ResNet-50 deep learning model..."):
            model = get_model()
            if model is None:
                st.error("Failed to load model.")
                st.stop()
            results = predict_leaf(model, selected_image, class_names)
            st.session_state["results"] = results
            st.session_state["analyzed_source"] = image_source_label

    if "results" in st.session_state:
        results = st.session_state["results"]
        top_raw_class, top_conf = results[0]
        crop_name, disease_name = format_label(top_raw_class)
        info = get_disease_info(top_raw_class)
        is_healthy = (info.get("status") == "Healthy")

        # Diagnosis Header Card
        st.markdown("### 🩺 Diagnostic Report")
        
        c1, c2, c3 = st.columns([1.6, 1.2, 1])
        with c1:
            st.markdown(f"**Crop Detected:** `{crop_name}`")
            st.markdown(f"**Condition:** `{disease_name}`")
        with c2:
            if is_healthy:
                st.markdown('<div class="badge-healthy">🟢 HEALTHY PLANT</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="badge-diseased">🔴 DISEASE DETECTED</div>', unsafe_allow_html=True)
        with c3:
            st.metric("Confidence Score", f"{top_conf:.2f}%")

        st.progress(min(max(top_conf / 100.0, 0.0), 1.0))

        # Tabs for Advisory, Probabilities, Specs
        tab_treat, tab_probs, tab_tech = st.tabs([
            "📋 Symptoms & Treatment Guide",
            "📊 Probability Breakdown (Top 5)",
            "ℹ️ Technical Inspection"
        ])

        with tab_treat:
            st.markdown(f"#### Condition Overview: {crop_name} — {disease_name}")
            st.write(info.get("description", "No description available."))

            col_sym, col_cau = st.columns(2)
            with col_sym:
                st.markdown('<div class="section-header">🔍 Key Symptoms to Look For</div>', unsafe_allow_html=True)
                st.info(info.get("symptoms", "Check for discoloration or spots."))
            with col_cau:
                st.markdown('<div class="section-header">🌧️ Environmental Causes</div>', unsafe_allow_html=True)
                st.warning(info.get("causes", "Pathogen development favored by ambient moisture and temperature."))

            col_rx, col_prev = st.columns(2)
            with col_rx:
                st.markdown('<div class="section-header">💊 Treatment & Remedies</div>', unsafe_allow_html=True)
                st.success(info.get("treatment", "Consult local agricultural extension specialists."))
            with col_prev:
                st.markdown('<div class="section-header">🛡️ Prevention & Best Practices</div>', unsafe_allow_html=True)
                st.info(info.get("prevention", "Maintain sanitization, crop rotation, and optimal spacing."))

        with tab_probs:
            st.markdown("#### Confidence Across Top 5 Classes")
            for rank, (name, pct) in enumerate(results, 1):
                p_crop, p_dis = format_label(name)
                c_lbl, c_bar = st.columns([2, 3])
                with c_lbl:
                    st.write(f"**{rank}. {p_crop}** — {p_dis}")
                with c_bar:
                    st.progress(min(max(pct / 100.0, 0.0), 1.0), text=f"{pct:.2f}%")

        with tab_tech:
            st.markdown("#### Deep Learning Model Inference Summary")
            st.json({
                "Model Path": str(MODEL_PATH),
                "Model Architecture": "ResNet-50 (Transfer Learning)",
                "Input Dimensions": f"224 × 224 × 3",
                "Preprocess": "Keras ResNet50 caffe mode",
                "Top Predicted Class": top_raw_class,
                "Confidence Percentage": f"{top_conf:.4f}%",
                "Total Classes": len(class_names)
            })

# Footer
st.divider()
st.markdown(
    "<center><small style='color: #777;'>PlantGuard AI • Powered by ResNet-50 & Streamlit • PlantVillage 38 Classes</small></center>",
    unsafe_allow_html=True
)
