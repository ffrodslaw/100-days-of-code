import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}").text
soup = BeautifulSoup(response, "html.parser")
song_titles = soup.select("li ul li h3")
titles_list = [song.get_text(strip=True) for song in song_titles]

###############################

# Spotify set-up

# credentials are saved in environment variables SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
# set env. variable SPOTPY_REDIRECT_URI to uri you used in your app's settings
scope = "playlist-modify-public"
USER = os.environ.get("SPOTIFY_USER")

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials)
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# create playlist
playlist_name = f"Billboard Hot 100 - {date}"
spotify.user_playlist_create(user=USER,
                             name=playlist_name,
                             public=True,
                             description="Automatically generated with Python")

# get song uris
uris = []
for song in song_titles:
    try:
        result = spotify.search(q=song)
        uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print("Song not found.")

# find correct playlist id
playlists = spotify.user_playlists(user=USER)["items"]
playlist_id = [playlist["id"] for playlist in playlists if playlist["name"] == playlist_name][0]

# add songs
spotify.user_playlist_add_tracks(user=USER,
                                 playlist_id=playlist_id,
                                 tracks=uris)