from PIL import Image
import os

# Directories
input_dirs = ["data/train", "data/validation"]
target_size = (48,48)

for input_dir in input_dirs:
    for mood in os.listdir(input_dir):
        mood_dir = os.path.join(input_dir, mood)
        if os.path.isdir(mood_dir):
            for img_name in os.listdir(mood_dir):
                img_path = os.path.join(mood_dir, img_name)
                try:
                    img = Image.open(img_path).convert('L')  # convert to grayscale
                    img = img.resize(target_size)
                    img.save(img_path)  # overwrite original
                except Exception as e:
                    print(f"Skipping {img_path}: {e}")

print("All images preprocessed to 48x48 grayscale.")
