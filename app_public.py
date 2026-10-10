import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 Plant Disease Detection")

st.write(
    "An AI-powered application designed to identify "
    "plant diseases from leaf images using deep learning."
)

st.subheader("📷 Upload a Plant Leaf")

uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Plant Leaf",
        use_container_width=True
    )

    # Preprocess the image for a 128 × 128 input
    resized_image = image.resize((128, 128))
    image_array = np.array(resized_image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    st.subheader("🔬 Image Preprocessing")
    st.write(f"Image input shape: {image_array.shape}")
    st.write("Pixel values are normalized to the range 0–1.")

    st.info(
        "The trained classification model and private "
        "prediction resources are intentionally excluded "
        "from this public showcase version."
    )

st.caption(
    "Project showcase: CNN-based plant disease classification "
    "with TensorFlow, Keras, and Streamlit."
)