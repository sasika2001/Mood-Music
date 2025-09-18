import json
import os
from typing import List

DATA_FILE = "data/moods.json"

# Load moods from file or use default
if os.path.exists(DATA_FILE):
    with open(DATA_FILE) as f:
        mood_mapping = json.load(f)
else:
    # Include all 7 moods with common synonyms
    mood_mapping = {
        "happy": ["joyful", "cheerful", "delighted", "upbeat"],
        "sad": ["blue", "down", "melancholy", "unhappy"],
        "angry": ["mad", "frustrated", "furious", "annoyed"],
        "fear": ["scared", "anxious", "afraid", "nervous"],
        "disgust": ["grossed out", "repulsed", "unpleasant", "distasteful"],
        "surprise": ["shocked", "amazed", "astonished", "startled"],
        "neutral": ["calm", "chill", "peaceful", "relaxed"]
    }

all_moods = list(mood_mapping.keys())

def classify_mood(user_mood: str) -> str:
    """Return the standard mood based on user input or synonyms."""
    user_mood = user_mood.lower()
    for mood, synonyms in mood_mapping.items():
        if user_mood == mood or user_mood in synonyms:
            return mood
    return None

def save_moods():
    """Save current moods to the JSON file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(mood_mapping, f, indent=4)

def add_manual_mood(new_mood: str, synonyms: List[str] = []):
    """Add a new mood manually with optional synonyms."""
    new_mood = new_mood.lower()
    if new_mood not in all_moods:
        mood_mapping[new_mood] = [s.lower() for s in synonyms]
        all_moods.append(new_mood)
        save_moods()  # Save automatically
    return all_moods
