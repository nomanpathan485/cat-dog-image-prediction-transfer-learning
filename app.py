from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
model = load_model("cat-dog-transfer-learning/cat_dog_transfer_model.keras")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    img_file = request.files["image"]

    img_path = "temp.jpg"
    img_file.save(img_path)

    img = image.load_img(
        img_path,
        target_size=(128,128)
    )

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    prediction = model.predict(img_array)

    score = prediction[0][0]

    if score > 0.5:
        result = "Dog"
        confidence = score * 100
    else:
        result = "Cat"
        confidence = (1 - score) * 100

    return f"""
    if confidence < 70:
    note = "Low Confidence Prediction"
    else:
    note = "High Confidence Prediction"
    <h1>Prediction: {result}</h1>
    <h2>Confidence: {confidence:.2f}%</h2>
    <a href="/">Try Another Image</a>
    """
if __name__ == "__main__":
    app.run(debug=True)