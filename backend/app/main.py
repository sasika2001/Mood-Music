from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from typing import List
import shutil

from models import predict_mood
from utils import classify_mood, add_manual_mood, all_moods
from music_recommender import get_spotify_tracks

from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI(title="Mood Music AI")

# Mount the frontend folder correctly (adjust path from backend/app to frontend)
app.mount("/frontend", StaticFiles(directory="../../frontend", html=True), name="frontend")

# --------------------
# ROUTES
# --------------------

@app.get("/moods")
def get_moods():
    """Return all available moods."""
    return {"moods": all_moods}

@app.post("/recommend/selfie")
def recommend_by_selfie(file: UploadFile = File(...)):
    """Recommend music based on selfie."""
    # Save uploaded file temporarily
    file_location = f"data/{file.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Predict mood from image
    mood = predict_mood(file_location)
    tracks = get_spotify_tracks(mood)
    return {"mood": mood, "tracks": tracks}

@app.post("/recommend/manual")
def recommend_by_manual(mood: str = Form(...)):
    """Recommend music based on manual mood input."""
    classified_mood = classify_mood(mood)
    if not classified_mood:
        raise HTTPException(
            status_code=404,
            detail="Mood not recognized. Use /add_mood to add it manually."
        )
    tracks = get_spotify_tracks(classified_mood)
    return {"mood": classified_mood, "tracks": tracks}

@app.post("/add_mood")
def add_mood_endpoint(mood: str = Form(...), synonyms: List[str] = Form([])):
    """Add a new manual mood."""
    updated_moods = add_manual_mood(mood, synonyms)
    return {"message": f"Mood '{mood}' added successfully!", "all_moods": updated_moods}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify "http://127.0.0.1:5500" if using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)