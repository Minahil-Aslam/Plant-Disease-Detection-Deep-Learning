# 🌿 Plant Disease Detection Using Deep Learning

A deep learning project that explores plant disease classification from leaf images using Convolutional Neural Networks (CNN), TensorFlow, and Streamlit.

## 📌 Project Overview

This project was developed to explore how AI can assist in identifying plant diseases from leaf images.

The complete application accepts a leaf image and uses a trained CNN model to predict a disease class, display a confidence score, and provide general disease information and treatment suggestions.

## ✨ Key Features

- Upload plant leaf images
- Image resizing and pixel normalization
- CNN-based multi-class image classification
- Prediction confidence score
- Disease descriptions and general treatment guidance
- Interactive Streamlit interface

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Convolutional Neural Networks (CNN)
- NumPy
- Pillow
- Streamlit

## 🧠 Model Information

- **Architecture:** Convolutional Neural Network (CNN)
- **Input image size:** 128 × 128 pixels
- **Classification categories:** 38
- **Dataset:** PlantVillage
- **Task:** Multi-class plant disease image classification

## 📂 Public Repository Contents

- `app_public.py` — public showcase demonstrating the Streamlit interface and image preprocessing.
- `README.md` — project documentation and setup information.

The trained model and supporting prediction resources are intentionally kept private. As a result, the public showcase file does not perform actual disease predictions.

## ▶️ Run the Public Showcase

Install the required packages:

```bash
pip install streamlit pillow numpy
```

Run the showcase:

```bash
streamlit run app_public.py
```

This runs the public image-upload and preprocessing demonstration. It does not load the private trained model or generate disease predictions.

## 📸 Application Screenshots

Screenshots of the application interface and example disease prediction results are available in the repository files.
## ⚠️ Disclaimer

Model predictions may be incorrect for some images. Disease information and treatment suggestions should be treated as general guidance, not as a substitute for professional agricultural advice.

## 👩‍💻 Author

**Minahil Aslam**

Artificial Intelligence | Machine Learning | Deep Learning
