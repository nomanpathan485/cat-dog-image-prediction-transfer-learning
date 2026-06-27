"""
predict.py — Standalone inference for the Cat vs Dog transfer-learning model.

Usage:
    python predict.py path/to/image.jpg
"""

import os
import sys
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "cat_dog_transfer_model.keras")
IMG_SIZE = (128, 128)
THRESHOLD = 0.5


def predict(img_path: str):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Image not found: {img_path}")

    model = load_model(MODEL_PATH)

    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = np.expand_dims(image.img_to_array(img), axis=0)

    score = float(model.predict(img_array)[0][0])        # P(dog)
    label = "Dog" if score > THRESHOLD else "Cat"
    confidence = score * 100 if score > THRESHOLD else (1 - score) * 100

    emoji = "🐶" if label == "Dog" else "🐱"
    print(f"{emoji}  Prediction : {label}")
    print(f"    Confidence : {confidence:.2f}%")
    return label, confidence


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py <path-to-image>")
        sys.exit(1)
    predict(sys.argv[1])