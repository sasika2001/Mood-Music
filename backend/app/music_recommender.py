import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Spotify authentication
auth_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)
sp = Spotify(auth_manager=auth_manager)

# Mood-to-keyword mapping for mood-lifting or relaxing recommendations
MOOD_KEYWORDS = {
    "happy": "happy upbeat energetic pop dance",          # Already happy → energetic songs
    "sad": "calm soothing mellow acoustic soft",          # Sad → relaxing songs
    "angry": "calm relaxing soft chill mellow",           # Angry → calm/relaxing songs
    "fear": "calm relaxing peaceful ambient soft",        # Fear → calming songs
    "disgust": "happy fun energetic upbeat pop",          # Disgust → uplifting songs
    "surprise": "fun energetic exciting upbeat",         # Surprise → fun/exciting songs
    "neutral": "chill ambient soft relaxing lo-fi"        # Neutral → chill/soft songs
}

def get_spotify_tracks(mood: str, limit: int = 10):
    """Fetch songs for the given mood from Spotify using keywords."""
    query = MOOD_KEYWORDS.get(mood.lower(), mood)  # fallback to mood word
    try:
        results = sp.search(q=query, type='track', limit=limit)
    except Exception as e:
        print(f"Error fetching tracks from Spotify: {e}")
        return []

    tracks = []
    for item in results['tracks']['items']:
        tracks.append({
            "name": item['name'],
            "artist": item['artists'][0]['name'],
            "url": item['external_urls']['spotify']
        })
    return tracks
