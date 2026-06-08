# Cat vs Dog Image Classifier (CNN + Transfer Learning)

This project is a simple image classifier that predicts whether an image contains a cat or a dog.

The goal of this project was not just to build a working model, but to understand why transfer learning is preferred over training CNNs from scratch in real world applications.

---

## What I Did

I first trained a CNN model from scratch. It gave around **76% accuracy**, but it was not very stable on new images.

After that, I used **MobileNetV2 (Transfer Learning)** and fine-tuned it for this dataset. This improved performance to around **96.5% validation accuracy**.

---

## What I Learned

- Training CNNs from scratch is useful for learning, but not always efficient for real datasets  
- Pre trained models already learn general image features, so transfer learning works better  
- MobileNetV2 is lightweight and performs well even on small datasets  
- **Global Max Pooling** can work better than Flatten because it reduces overfitting  
- Small architecture changes can significantly affect performance  

---

## Tech Stack

- Python  
- TensorFlow / Keras  
- Flask  
- NumPy  
- Pillow  
- HTML

---

## How It Works

- User uploads an image through a web page  
- Flask backend receives the image  
- Image is preprocessed and passed to the trained model  
- Model predicts cat or dog  
- Result is displayed on the screen  

---

## Results

- CNN from scratch: ~76% accuracy  
- MobileNetV2: ~96.5% validation accuracy  

---

## Note

This project helped me understand the gap between learning deep learning concepts and applying them in practical scenarios.