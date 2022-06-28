import json
import logging
import spotipy
import config
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyBackend:
    def __init__(self):
        self.spotify_session = None

    def create_session(self):
        self.spotify_session = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=config.spotify_key,
                client_secret=config.spotify_secret
            )
        )
    
    def playlist_songs(self, url):
        songs = self.spotify_session.playlist_items(
            playlist_id=url, additional_types=('track',))['items']
        return songs
