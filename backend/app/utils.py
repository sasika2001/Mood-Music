import json
import os
from typing import List

DATA_FILE = "data/moods.json"

# Load moods from file or use default
if os.path.exists(DATA_FILE):
    with open(DATA_FILE) as f:
        mood_mapping = json.load(f)
else:
    mood_mapping = {
        "happy": ["joyful", "cheerful", "delighted"],
        "sad": ["blue", "down", "melancholy"],
        "relaxed": ["calm", "chill", "peaceful"]
    }

all_moods = list(mood_mapping.keys())

def classify_mood(user_mood: str) -> str:
    """Return standard mood based on user input."""
    user_mood = user_mood.lower()
    for mood, synonyms in mood_mapping.items():
        if user_mood == mood or user_mood in synonyms:
            return mood
    return None

def save_moods():
    """Save current moods to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(mood_mapping, f)

def add_manual_mood(new_mood: str, synonyms: List[str] = []):
    """Add a new mood manually."""
    new_mood = new_mood.lower()
    if new_mood not in all_moods:
        mood_mapping[new_mood] = [s.lower() for s in synonyms]
        all_moods.append(new_mood)
        save_moods()  # Save automatically
    return all_moods
