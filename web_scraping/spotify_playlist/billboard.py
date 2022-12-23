import requests
import datetime as dt
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()


# user_date = input("Which year do want to make a playlist of? Type the date in this format YYYY-MM-DD: ")
user_date: str = "2016-06-01"
# not that useful now but can be used to validate date before making a get request
user_date: list = user_date.split("-")

date = dt.datetime(int(user_date[0]), int(user_date[1]), int(user_date[2]))
date_str: str = date.strftime("%Y-%m-%d")

billboard_site_data = requests.get(
    f"https://www.billboard.com/charts/hot-100/{date_str}/")

billboard_soup = BeautifulSoup(billboard_site_data.text, "lxml")

top_100_tracks = billboard_soup.find_all(
    name="h3", id="title-of-a-story", class_="a-no-trucate")
top_100_artists = billboard_soup.find_all(name="span", class_="a-no-trucate")

songs = []

for i in range(100):
    obj = {
        "artist": top_100_artists[i].getText().strip(),
        "song": top_100_tracks[i].getText().strip(),
        "spotify_url" : ""
    }
    songs.append(obj)

# Spotify auth
spotify_client_id: str = os.environ.get("SPOTIFY_CLIENT_ID")
spotify_client_secret: str = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.environ.get("REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))


# search for songs on spotify
spotify_search_list: list = []
for song in songs:
    artist: str = song["artist"]
    track_title: str = song["song"]
    search_results = sp.search(q=f"artist:{artist} track: {track_title}", type=[
                               "track"], limit=5, market="US")
    search_tracks = search_results["tracks"]
    if search_tracks["total"] > 0:
        song["spotify_url"] = (search_tracks["items"][0]["external_urls"])


# get spotify user id
spotify_user_id = sp.current_user()["id"]


# create a playlist for the user
playlist = sp.user_playlist_create(spotify_user_id, f"{date_str} Billboard 100", public=False,
                                   description=f"A playlist for the billboard top 100 in the week of {date_str}")

# playlist_id =  '6i6YGidRYLdegdtmylNSGc'

#add songs to the playlist
songs_urls = []
for song in songs:
    if song["spotify_url"] != "":
        songs_urls.append(song["spotify_url"]["spotify"])


playlist_result = sp.playlist_add_items(playlist_id=playlist["id"],items=songs_urls,position=None)

pprint(sp.playlist(playlist_id=playlist["id"]["total"]))
