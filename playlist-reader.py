from types import prepare_class
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
import tidal_backend
import tidalapi
import logging
import json

songs = []

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=config.spotify_key,
        client_secret=config.spotify_secret
    )
)

def playlist_songs(url):
    songs = sp.playlist_items(
        playlist_id=url, additional_types=('track',))['items']
    print(songs)
    return songs



def main():
    # songs = playlist_songs(
    #     url="https://open.spotify.com/playlist/7ozIozDp260fjNOZy1yzRG?si=6c9576eb3d3e46dd"
    # )

    tidal = tidal_backend.TidalBackend()
    tidal.oauth_session()



if __name__ == "__main__":
    main()
