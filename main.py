from bs4 import BeautifulSoup
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
CLASS = "chart-element__information__song text--truncate color--primary"

spot = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = spot.current_user()["id"]

date = input("Which day would you like to travel to? (YYYY-MM-DD): ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(billboard_url)
website = response.text
soup = BeautifulSoup(website, "html.parser")
songs = [song.text for song in soup.find_all(name="span", class_=CLASS)]

song_uris = []
for song in songs:
    result = spot.search(q=f"track:{song} year:{date.split('-')[0]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} isn't available on Spotify right now. Skipped.")

playlist = spot.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
spot.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
