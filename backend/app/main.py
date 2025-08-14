from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from .music_recommender import MusicRecommender, MOODS, MOOD_SYNONYMS


class Track(BaseModel):
    title: str
    artist: str
    url: Optional[str] = None


class RecommendRequest(BaseModel):
    mood: str = Field(
        ...,
        description="Mood for music recommendation",
        examples=["happy", "sad", "relaxed", "energetic", "romantic", "chill", "motivational", "nostalgic"]
    )


class RecommendResponse(BaseModel):
    mood: str
    tracks: List[Track]


app = FastAPI(
    title="Music Recommender API",
    description="API for music recommendations based on mood",
    version="1.1.0"
)


@app.get("/", tags=["Root"])
def health():
    return {"message": "Welcome to the Music Recommender API"}


@app.post("/recommend", response_model=RecommendResponse, tags=["Recommendations"])
def recommend_tracks(request: RecommendRequest):
    mood_input = request.mood.lower().strip()

    # Convert synonyms to main mood
    if mood_input in MOOD_SYNONYMS:
        mood_input = MOOD_SYNONYMS[mood_input]

    if mood_input not in MOODS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid mood '{request.mood}'. Try one of: {', '.join(MOODS)}"
        )

    recommender = MusicRecommender()
    tracks = recommender.recommend_tracks(mood_input)

    return RecommendResponse(mood=mood_input, tracks=tracks)


@app.get("/moods", response_model=List[str], tags=["Moods"])
def get_moods():
    return MOODS
