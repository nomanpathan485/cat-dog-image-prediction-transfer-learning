import os
import uuid
from flask import Flask, render_template, request, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# ----------------------------------------------------------------------
# Robust paths so the app runs regardless of the current working directory
# ----------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "cat_dog_transfer_model.keras")
UPLOAD_DIR = os.path.join(BASE_DIR, "static", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(__name__)
model = load_model(MODEL_PATH)

# Reusable prediction pipeline
def predict_image(img_path: str):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = np.expand_dims(image.img_to_array(img), axis=0)
    score = float(model.predict(img_array)[0][0])        # P(dog)
    label = "Dog" if score > 0.5 else "Cat"
    confidence = score * 100 if score > 0.5 else (1 - score) * 100
    tier = "High Confidence" if confidence >= 70 else "Low Confidence"
    return label, confidence, tier


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    img_file = request.files.get("image")
    if img_file is None or img_file.filename == "":
        return render_template("index.html", error="Please upload an image.")

    # Save with a unique name so multiple users don't clobber each other
    ext = os.path.splitext(img_file.filename)[1].lower() or ".jpg"
    saved_name = f"{uuid.uuid4().hex}{ext}"
    saved_path = os.path.join(UPLOAD_DIR, saved_name)
    img_file.save(saved_path)

    label, confidence, tier = predict_image(saved_path)
    image_url = url_for("static", filename=f"uploads/{saved_name}")

    return render_template(
        "index.html",
        prediction=label,
        confidence=f"{confidence:.2f}%",
        tier=tier,
        image_url=image_url,
    )


if __name__ == "__main__":
    app.run(debug=True)