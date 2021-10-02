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
        """Sends the first and second half of each token to the ticket response to keep the token alive."""
        data = {"authorization": f"Session {self.staytoken}:{self.token}", "Accept": "application/json"}
        url = f"{self.base_url}/support/tickets/"
        req = requests.get(url, headers=data)
        json_data = json.loads(req.text)
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return json_data

    def collect_loot(self):
        """Collects any sold ally gold from the treasury."""
        data = {"authorization": f"Bearer {self.token}", "Accept": "application/json"}
        url = f"{self.base_url}/game/resource/collect_unlootable_resources/"
        req = requests.get(url, headers=data)
        json_data = json.loads(req.text)
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return json_data

    def get_user_by_name(self, username: str) -> Dict:
        """Searches the users api using username."""
        url = f"{self.base_url}/game/user/search_by_name/"
        data = {"username": username}
        return self._post(url, data)

    def get_ally_by_name(self, username: str) -> Dict:
        """Searches the ally api using username."""
        url = f"{self.base_url}/game/ally/search_allies_by_username/"
        data = {"ally_username": username}
        return self._post(url, data)

    def get_clan_by_id(self, group_id: int) -> Dict:
        """Searches the clan api for a group with given group_id."""
        url = f"{self.base_url}/game/group/get_group/"
        data = {"group_id": group_id}
        return self._post(url, data)
	
    def get_allies_by_price(self, price: int, offset: int = 0) -> Dict:
        """Searches the ally api using max cost and page offset."""
        url = f"{self.base_url}/game/ally/search_allies"
        data = {'max_cost': price, 'offset': offset}
        return self._post(url, data)

    def buy_ally(self, username: str, cost: int) -> Dict:
        """Purchases an ally by ID and expected cost to the current logged in account."""
        url = f"{self.base_url}/game/ally/buy_ally"
        data = {'ally_user_id': username, 'expected_cost': cost}
        return self._post(url, data)

    def poll_chat(self):
        """Polls the logged in users global/clan and announcement chats.
        Currently only returning the global chat."""
        data = {"authorization": f"Bearer {self.token}", "Accept": "application/json"}
        url = f"{self.base_url}/game/poll/chat"
        req = requests.get(url, headers=data)
        json_data = json.loads(req.text)
        chats = json_data['global_messages']
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return chats

    def poll_realm_list(self):
        """Polls the list of active realms usercounts, names and descriptions, returns the shards response only"""
        data = {"authorization": f"Bearer {self.token}", "Accept": "application/json"}
        url = f"{self.base_url}/game/shard/get_transferable_shards/"
        req = requests.get(url, headers=data)
        json_data = json.loads(req.text)
        realms = json_data['shards']
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return realms

    def poll_group_power_leaderboard(self):
        """Polls the clans top might/power leaderboards for given tokens realm"""
        data = {"authorization": f"Bearer {self.token}", "Accept": "application/json"}
        url = f"{self.base_url}/game/leaderboard/get_group_power_leaderboard"
        req = requests.get(url, headers=data)
        json_data = json.loads(req.text)
        group_power_leaderboard = json_data['group_power_leaderboard_leaders']
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return group_power_leaderboard
        
    def poll_group_troopkill_leaderboard(self):
        """Polls the clans top troop kills leaderboards for given tokens realm"""
        data = {"authorization": f"Bearer {self.token}", "Accept": "application/json"}
        url = f"{self.base_url}/game/leaderboard/get_group_troopkill_leaderboard"
        req = requests.get(url, headers=data)
        json_data = json.loads(req.text)
        group_troopkill_leaderboard = json_data['group_troopkill_leaderboard_leaders']
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return group_troopkill_leaderboard

    def poll_user_power_leaderboard(self):
        """Polls the user top might/power leaderboards for given tokens realm"""
        data = {"authorization": f"Bearer {self.token}", "Accept": "application/json"}
        url = f"{self.base_url}/game/leaderboard/get_user_power_leaderboard"
        req = requests.get(url, headers=data)
        json_data = json.loads(req.text)
        user_power_leaderboard = json_data['user_power_leaderboard_leaders']
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return user_power_leaderboard

    def poll_user_troopkill_leaderboard(self):
        """Polls the user troop kills leaderboards for given tokens realm"""
        data = {"authorization": f"Bearer {self.token}", "Accept": "application/json"}
        url = f"{self.base_url}/game/leaderboard/get_user_troopkill_leaderboard"
        req = requests.get(url, headers=data)
        json_data = json.loads(req.text)
        user_troopkill_leaderboard = json_data['user_troopkill_leaderboard_leaders']
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return user_troopkill_leaderboard

    def poll_mail(self):
        """Polls the logged in users mail."""
        data = {"authorization": f"Bearer {self.token}", "Accept": "application/json"}
        url = f"{self.base_url}/game/poll/mail"
        req = requests.get(url, headers=data)
        json_data = json.loads(req.text)
        mails = json_data['mails']
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return mails

    def _post(self, url: str, data: Dict) -> Dict:
        response = requests.post(url, headers=self.headers, data=data)
        json_data = json.loads(response.text)
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return json_data

    def fetch_world(self, lowerbound: int):
        """Fetches 20 chunks of world map data only taking the 'sites' chunk of response.
        20 is the api limit."""
        tiles = []
        url = f"{self.base_url}/game/nonessential/poll_segments_realm_state"
        data = {"segment_ids": [i for i in range(lowerbound, lowerbound + 20)]}
        req = requests.post(url, headers=self.headers, data=data)
        json_data = req.json()
        sites = json_data["world_state"]["sites"]
        for tile in sites:
            tiles.append(sites[tile])
        data["segment_ids"] = [d + 20 for d in data["segment_ids"]]
        return tiles

    def get_clan_for_user(self):
        """Sends request to api to grab the current clan for logged in user, pulls group_id from response"""
        data = {"authorization": f"Bearer {self.token}", "Accept": "application/json"}
        url = f"{self.base_url}/game/group/get_group_for_user/"
        req = requests.get(url, headers=data)
        json_data = json.loads(req.text)
        group_id = json_data['id']
        if json_data.get('exception'):
            raise TokenException(json_data['exception'])
        return group_id

    def get_clan_requests(self):
        """Sends request to api to grab the requests to join the current clan for logged in user.
        Requires High enough rank in clan or not authorized exception"""
        group_id = self.get_clan_for_user()
        url = f"{self.base_url}/game/group/get_join_requests/"
        data = {"group_id": group_id}
        return self._post(url, data)

    def message_clan(self, message: str) -> Dict:
        """Sends given message to current tokens clan chat"""
        group_id = self.get_clan_for_user()
        url = f"{self.base_url}/game/message/send_group_chat/"
        data = {"group_id": group_id, "message": message}
        return self._post(url, data)