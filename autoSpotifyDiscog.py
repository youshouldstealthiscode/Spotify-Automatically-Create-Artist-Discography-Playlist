import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

client_id = '<your_client_id>'
client_secret = '<your_client_secret>'
redirect_uri = 'http://localhost:8000/'

scope = 'user-library-read playlist-modify-public playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

def get_artist_id(artist_name):
    result = sp.search(q=f'artist:{artist_name}', type='artist')
    artist = result['artists']['items'][0]
    return artist['id'], artist['name']

def get_all_artist_releases(artist_id):
    albums = []
    result = sp.artist_albums(artist_id, album_type='album,single,appears_on,compilation')
    while result['next']:
        albums.extend(result['items'])
        result = sp.next(result)

    albums.extend(result['items'])
    return albums

def filter_and_sort_releases(releases):
    unique_albums = {}
    for release in releases:
        if release['name'] not in unique_albums:
            unique_albums[release['name']] = release

    sorted_releases = sorted(unique_albums.values(), key=lambda x: (x['release_date'], x['added_at']))
    return sorted_releases

def create_discography_playlist(artist_name, releases):
    user_id = sp.current_user()['id']
    playlist_name = f"{artist_name} Discography"
    playlist = sp.user_playlist_create(user_id, playlist_name, public=True, description=f'{artist_name} complete discography.')

    for release in releases:
        tracks = sp.album_tracks(release['id'])['items']
        track_ids = [track['id'] for track in tracks]
        sp.playlist_add_items(playlist['id'], track_ids)

    return playlist['id']

def main():
    artist_name = input("Enter the artist name: ")
    artist_id, actual_artist_name = get_artist_id(artist_name)
    releases = get_all_artist_releases(artist_id)
    sorted_releases = filter_and_sort_releases(releases)
    playlist_id = create_discography_playlist(actual_artist_name, sorted_releases)

    print(f"Successfully created a playlist titled '{actual_artist_name} Discography' with ID: {playlist_id}")

if __name__ == '__main__':
    main()
