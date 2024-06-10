import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

clients_credential_manager = SpotifyClientCredentials(client_id="#######", client_secret="#########")

sp = spotipy.Spotify(client_credentials_manager=clients_credential_manager)

data = sp.playlist_tracks("37i9dQZEVXbJiZcmkrIHGU")

#print(json.dumps(data, indent=4)) # returns a more readable format

track_name = data["items"][0]["track"]["album"]["name"]
artist_name = data["items"][0]["track"]["album"]["artists"][0]["name"]
release_date = data["items"][0]["track"]["album"]["release_date"]


track_list = []

for row in data["items"]:
    track_name = row["track"]["album"]["name"]
    artist_name = row["track"]["album"]["artists"][0]["name"]
    release_date = row["track"]["album"]["release_date"]
    artist_element = {"Artist Name": artist_name, "Track Name": track_name, "Release Date": release_date}
    track_list.append(artist_element)

# print(json.dumps(album_name, indent=4))

print(track_list)
