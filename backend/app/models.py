from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import json

# Load the trained model
model = load_model('data/facial_mood_model.h5')

# Load class indices mapping
with open("data/class_indices.json", "r") as f:
    class_indices = json.load(f)

# Reverse it: { "angry": 0 } -> { 0: "angry" }
idx_to_class = {v: k for k, v in class_indices.items()}

def predict_mood(img_path: str) -> str:
    """Predict mood from a selfie image."""
    img = image.load_img(img_path, target_size=(48,48), color_mode="grayscale")
    img_array = image.img_to_array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    preds = model.predict(img_array)
    mood_index = np.argmax(preds)
    predicted_mood = idx_to_class[mood_index]   # ✅ Correct mapping
    
    return predicted_mood
