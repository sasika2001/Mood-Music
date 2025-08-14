from typing import List, Dict, Any

# Main playlists
MOOD_PLAYLISTS: Dict[str, List[Dict[str, Any]]] = {
    "happy": [
        {"title": "Happy Song 1", "artist": "Artist A", "url": "http://example.com/happy1"},
        {"title": "Happy Song 2", "artist": "Artist B", "url": "http://example.com/happy2"},
    ],
    "sad": [
        {"title": "Sad Song 1", "artist": "Artist C", "url": "http://example.com/sad1"},
        {"title": "Sad Song 2", "artist": "Artist D", "url": "http://example.com/sad2"},
    ],
    "relaxed": [
        {"title": "Relaxed Song 1", "artist": "Artist E", "url": "http://example.com/relaxed1"},
        {"title": "Relaxed Song 2", "artist": "Artist F", "url": "http://example.com/relaxed2"},
    ],
    "energetic": [
        {"title": "Energetic Song 1", "artist": "Artist G", "url": "http://example.com/energetic1"},
        {"title": "Energetic Song 2", "artist": "Artist H", "url": "http://example.com/energetic2"},
    ],
    "romantic": [
        {"title": "Romantic Song 1", "artist": "Artist I", "url": "http://example.com/romantic1"},
        {"title": "Romantic Song 2", "artist": "Artist J", "url": "http://example.com/romantic2"},
    ],
    "chill": [
        {"title": "Chill Song 1", "artist": "Artist K", "url": "http://example.com/chill1"},
        {"title": "Chill Song 2", "artist": "Artist L", "url": "http://example.com/chill2"},
    ],
    "motivational": [
        {"title": "Motivational Song 1", "artist": "Artist M", "url": "http://example.com/motivational1"},
        {"title": "Motivational Song 2", "artist": "Artist N", "url": "http://example.com/motivational2"},
    ],
    "nostalgic": [
        {"title": "Nostalgic Song 1", "artist": "Artist O", "url": "http://example.com/nostalgic1"},
        {"title": "Nostalgic Song 2", "artist": "Artist P", "url": "http://example.com/nostalgic2"},
    ],
}

# Synonyms mapping for flexible mood search
MOOD_SYNONYMS: Dict[str, str] = {
    "joyful": "happy",
    "cheerful": "happy",
    "content": "happy",
    "depressed": "sad",
    "blue": "sad",
    "calm": "relaxed",
    "peaceful": "relaxed",
    "romance": "romantic",
    "love": "romantic",
    "motivating": "motivational",
    "inspired": "motivational",
    "throwback": "nostalgic",
    "memories": "nostalgic"
}

MOODS = list(MOOD_PLAYLISTS.keys())


class MusicRecommender:
    def recommend_tracks(self, mood: str) -> List[Dict[str, Any]]:
        """Return a list of tracks for a given mood."""
        return MOOD_PLAYLISTS.get(mood, [])
