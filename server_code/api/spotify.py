##### SPOTIFY API #####
#
############################


##### MODULES #####
import requests
import json
import re
# import threading
# from threading import Event
# from time import sleep


##### VARS #####
TOKEN_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1/"


##### MAIN CLASS #####
class API:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client: tuple = (client_id, client_secret)
        self.headers = {}

    def get_access_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        payload = f"grant_type=client_credentials&client_id={self.client[0]}&client_secret={self.client[1]}"
        response = requests.request("POST", TOKEN_URL, headers=headers, data=payload)
        readable_response: dict = json.loads(response.text)
        access_token: str = readable_response["access_token"]
        return access_token

    def get_link_information(self, link):
        spotify_link_regex = r'https://open\.spotify\.com/(intl-[a-z]{2}/)?(track|album|artist|playlist)/([a-zA-Z0-9]+)'
        regex_match = re.match(spotify_link_regex, link)
        if regex_match:
            self.link_type = regex_match.group(2)
            self.spotify_id = regex_match.group(3)

    def get_id_data(self, link_type, spotify_id):
        url = f"{BASE_URL}{link_type}s/{spotify_id}"
        self.access_token = self.get_access_token()
        self.headers["Authorization"] = f"Bearer {self.access_token}"
        response = requests.request("GET", url, headers=self.headers)
        readable_response: dict = json.loads(response.text)
        print(readable_response)
