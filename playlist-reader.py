from types import prepare_class
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
import tidalapi

songs = []

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=config.spotify_key,
        client_secret=config.spotify_secret
    )
)

td = tidalapi.login(
    user=config.tidal_user,
    password=config.tidal_password
)

print(tidalapi.check_login())


def print_playlist_songs(url):
    songs = sp.playlist_items(
        playlist_id=url, additional_types=('track',))['items']
    for s in songs:
        songs.append(s)


def main():
    print_playlist_songs(
        url="https://open.spotify.com/playlist/7ozIozDp260fjNOZy1yzRG?si=6c9576eb3d3e46dd"
    )


if __name__ == "__main__":
    main()
