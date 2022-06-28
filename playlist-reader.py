import tidalapi
import tidal_backend
import spotify_backend


def main():
    spotify = spotify_backend.SpotifyBackend()
    spotify.create_session()
    songs = spotify.playlist_songs("https://open.spotify.com/playlist/0nl9sjINtq6dIVnPZIGvDt?si=e036722c51464ec0")

    tidal = tidal_backend.TidalBackend()
    tidal.oauth_session()
    songs_to_search = []
    for song in songs:
        songs_to_search.append(song['track']['name'] + " " + song['track']['artists'][0]['name'])
        
    songs_to_add = []
    for song in songs_to_search:
        songs_to_add.append(tidal.search_song(song))
    
    playlist = tidalapi.Playlist()
    print(playlist)

    



if __name__ == "__main__":
    main()
