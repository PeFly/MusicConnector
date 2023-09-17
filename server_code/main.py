import anvil.secrets
##### MUSIC CONNECTOR #####
# Translate music between streaming services
###########################


##### MODULES #####
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
import anvil.http
import anvil.secrets

import re
import json
import os
from api import spotify



##### VARS #####
secrets_file = "/MusicConnector/app/.secrets"
if os.path.exists(secrets_file):
  with open(secrets_file, "r") as secrets_file:
    secrets = json.load(secrets_file)["Spotify"]
  SPOTIFY_CLIENT_ID = secrets['CLIENT_ID']
  SPOTIFY_CLIENT_SECRET = secrets['CLIENT_SECRET']
else:
  SPOTIFY_CLIENT_ID = anvil.secrets.get_secret('Spotify.CLIENT_ID')
  SPOTIFY_CLIENT_SECRET = anvil.secrets.get_secret('Spotify.CLIENT_SECRET')


##### API OBJECTS #####
spotify_music = spotify.API(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)


##### CLIENT CALLABLE #####
@anvil.server.callable
def check_input(input_link):
  link_regex = r'https://open\.spotify\.com/(intl-[a-z]{2}/)?(track|album|artist|playlist)/([a-zA-Z0-9]+)'
  if re.match(link_regex, input_link):
    return True
  else:
    return False

@anvil.server.callable
def spotify_get_link_information(input_link):
  link_data = spotify_music.get_link_information(input_link)
  return link_data

@anvil.server.callable
def spotify_get_id_data(link_type, spotify_id):
  id_data = spotify_music.get_id_data(link_type, spotify_id)
  return id_data