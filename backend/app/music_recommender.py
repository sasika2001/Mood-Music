import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load .env
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Spotify authentication
auth_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)
sp = Spotify(auth_manager=auth_manager)

# Mood to keyword mapping
MOOD_KEYWORDS = {
    "happy": "happy upbeat energetic",
    "sad": "sad mellow calm",
    "angry": "angry intense rock",
    "fear": "dark suspense tense",
    "disgust": "gritty harsh",
    "surprise": "exciting unexpected",
    "neutral": "chill relaxing soft"
}

def get_spotify_tracks(mood: str, limit: int = 10):
    """Fetch songs for the given mood from Spotify using keywords."""
    query = MOOD_KEYWORDS.get(mood.lower(), mood)  # fallback to mood word
    results = sp.search(q=query, type='track', limit=limit)
    tracks = []
    for item in results['tracks']['items']:
        tracks.append({
            "name": item['name'],
            "artist": item['artists'][0]['name'],
            "url": item['external_urls']['spotify']
        })
    return tracks
