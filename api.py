import requests
import json
from typing import Dict
class TokenException(Exception):
    pass


class HeckfireApi(object):
    def __init__(
        self,
        user: str = None,
        password: str = None,
        client: str = "1.93",
        version: str = "2922",
        token: str = None,
        staytoken: str = None
    ):
        self.base_url = 'https://api.kingdomsofheckfire.com'
        self.user = user
        self.password = password
        self.client = client
        self.version = version
        self.staytoken = staytoken
        if token:
            self.token = token
        else:
            self.token = self.update_token()

        self.headers = {"Authorization": f"Bearer {self.token}", "Accept": "application/json"}

    def update_token(self):
        data = {
            "grant_type": "password",
            "client_version": self.client,
            "channel_id": 16,
            "client_id": "ata.kraken.heckfire",
            "client_secret": "n0ts0s3cr3t",
            "scope": "[]",
            "version": self.version,
            "include_tech_tree": "False",
            "username": self.user,
            "password": self.password
        }
        url = f"{self.base_url}/game/auth/oauth/"
        req = requests.post(url, data=data)
        if req.status_code == 200:
            res = req.json()
            self.token = res["access_token"].strip()
        else:
            error = req.json()
            print(error)
            message = error["exception"]
            raise TokenException(f"Failed to fetch token from heck api. Error: {message}")

    def stay_alive(self):
        data = {"authorization": f"Session {self.staytoken}:{self.token}", "Accept": "application/json"}
        url = f"{self.base_url}/support/tickets/"
        req = requests.get(url, headers=data)
        json_data = json.loads(req.text)
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return json_data

    def get_ally_by_name(self, username: str) -> Dict:
        url = f"{self.base_url}/game/ally/search_allies_by_username/"
        data = {"ally_username": username}
        return self._post(url, data)
	
    def get_allies_by_price(self, price: int, offset: int = 0) -> Dict:
        url = f"{self.base_url}/game/ally/search_allies"
        data = {'max_cost': price, 'offset': offset}
        return self._post(url, data)

    def _post(self, url: str, data: Dict) -> Dict:
        response = requests.post(url, headers=self.headers, data=data)
        json_data = json.loads(response.text)
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return json_data

    def fetch_world(self, lowerbound: int):
        tiles = []
        url = f"{self.base_url}/game/nonessential/poll_segments_realm_state"
        data = {"segment_ids": lowerbound}  # grab each section of the map in chunks
        req = requests.post(url, headers=self.headers, data=data)
        json_data = req.json()
        sites = json_data["world_state"]["sites"]
        for tile in sites:
            tiles.append(sites[tile])
        return tiles