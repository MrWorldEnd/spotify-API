import spotipy
import spotipy as spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id="CLIENT_ID   GET FROM SPOTIFY DASHBOARD",
                                               client_secret="SECRET_CLIENT_ID",
                                               redirect_uri="https://developer.spotify.com/",
                                               scope='user-read-playback-state,user-modify-playback-state'))
float
# Shows playing devices
res = sp.devices()
print(res)

# Change track
sp.start_playback(uris=['spotify:track:0HUTL8i4y4MiGCPId7M7wb'])