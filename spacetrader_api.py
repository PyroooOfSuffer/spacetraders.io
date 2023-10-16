import time
import requests
import os


def get_token():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "auth_token.txt")

    with open(file_path, "r") as file:
        file_content = file.read()
        return file_content


class ApiRequest:
    def __init__(self):
        self.auth_token = get_token()
        self.session = requests.session()
        self.base_url = "https://api.spacetraders.io/v2/"
        self.headers = {"Authorization": f"Bearer {self.auth_token}", "Accept": "application/json"}
        self.session.headers.update(self.headers)
        self.last_request_time = 0
        try:
            response = self.get_status()
            if response.status_code == 200:
                pass
            else:
                raise Exception
        except Exception as e:
            print(f"Error: {e}")

    def rate_limited(self, method: str, url: str, params: dict = None, json: dict = None):
        current_time = time.perf_counter()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < 0.5:
            sleep_time = 0.5 - time_since_last_request
            time.sleep(sleep_time)

        try:
            if method == "GET":
                response = self.session.get(url=url, params=params)
            elif method == "POST":
                response = self.session.post(url=url, params=params, json=json)
            elif method == "PATCH":
                response = self.session.patch(url=url, params=params, json=json)
            else:
                raise ValueError("Unsupported HTTP method")

            self.last_request_time = time.perf_counter()

            if response.status_code // 100 != 2:
                raise Exception(f"HTTP Error: {response.status_code}")

            return response.json()

        except Exception as e:
            print(f"Error: {e}")

    def register(self, symbol: str, faction: str = "COSMIC", email: str = None):
        if email is None:
            payload = {
                "symbol": symbol,
                "faction": faction
            }
        else:
            payload = {
                "symbol": symbol,
                "faction": faction,
                "email": email
            }
        url = f"{self.base_url}register"
        return requests.post(url=url, json=payload)  # as request cause old token/header can be invalid

    def get_status(self):
        url = self.base_url
        return requests.get(url=url)  # as request cause old token/header can be invalid

    def get_my_agent(self):
        url = f"{self.base_url}my/agent"
        return self.rate_limited(method="GET", url=url)

    def list_agent(self, page: int = 1, limit: int = 10):
        parameters = {"page": page, "limit": limit}
        url = f"{self.base_url}agents"
        return self.rate_limited(method="GET", url=url, params=parameters)

    def get_agent(self, agent_symbol: str):
        url = f"{self.base_url}agents/{agent_symbol}"
        return self.rate_limited(method="GET", url=url)

    def list_contracts(self, page: int = 1, limit: int = 10):
        parameters = {"page": page, "limit": limit}
        url = f"{self.base_url}my/contracts"
        return self.rate_limited(method="GET", url=url, params=parameters)

    def get_contract(self, contract_id: str):
        url = f"{self.base_url}my/contracts/{contract_id}"
        return self.rate_limited(method="GET", url=url)

    def accept_contract(self, contract_id: str):
        url = f"{self.base_url}my/contracts/{contract_id}/accept"
        return self.rate_limited(method="POST", url=url)

    def deliver_cargo_to_contract(self, contract_id: str, ship_symbol: str, trade_symbol: str, units: int):
        payload = {
            "shipSymbol": ship_symbol,
            "tradeSymbol": trade_symbol,
            "units": units
        }
        url = f"{self.base_url}my/contracts/{contract_id}/deliver"
        return self.rate_limited(method="POST", url=url, json=payload)

    def fulfill_contract(self, contract_id: str):
        url = f"{self.base_url}my/contracts/{contract_id}/fulfill"
        return self.rate_limited(method="POST", url=url)

    def list_faction(self, page: int = 1, limit: int = 10):
        parameters = {"page": page, "limit": limit}
        url = f"{self.base_url}factions"
        return self.rate_limited(method="GET", url=url, params=parameters)

    def get_faction(self, faction_symbol: str):
        url = f"{self.base_url}factions/{faction_symbol}"
        return self.rate_limited(method="GET", url=url)

    def list_ships(self, page: int = 1, limit: int = 10):
        parameters = {"page": page, "limit": limit}
        url = f"{self.base_url}my/ships"
        return self.rate_limited(method="GET", url=url, params=parameters)

    def purchase_ship(self, ship_type: str, waypoint_symbol: str):
        payload = {
            "shipType": ship_type,
            "waypointSymbol": waypoint_symbol
        }
        url = f"{self.base_url}my/ships"
        return self.rate_limited(method="POST", url=url, json=payload)

    def get_ship(self, ship_symbol: str):
        url = f"{self.base_url}my/ships/{ship_symbol}"
        return self.rate_limited(method="GET", url=url)

    def get_ship_cargo(self, ship_symbol: str):
        url = f"{self.base_url}my/ships/{ship_symbol}/cargo"
        return self.rate_limited(method="GET", url=url)

    def orbit_ship(self, ship_symbol: str):
        url = f"{self.base_url}my/ships/{ship_symbol}/orbit"
        return self.rate_limited(method="POST", url=url)

    def ship_refine(self, ship_symbol: str, produce: str):
        payload = {
            "produce": produce
        }
        url = f"{self.base_url}my/ships/{ship_symbol}/refine"
        return self.rate_limited(method="POST", url=url, json=payload)

    def create_chart(self, ship_symbol: str):
        url = f"{self.base_url}my/ships/{ship_symbol}/chart"
        return self.rate_limited(method="POST", url=url)

    def get_ship_cooldown(self, ship_symbol: str):
        url = f"{self.base_url}my/ships/{ship_symbol}/cooldown"
        return self.rate_limited(method="GET", url=url)

    def dock_ship(self, ship_symbol: str):
        url = f"{self.base_url}my/ships/{ship_symbol}/dock"
        return self.rate_limited(method="POST", url=url)

    def create_survey(self, ship_symbol: str):
        url = f"{self.base_url}my/ships/{ship_symbol}/survey"
        return self.rate_limited(method="POST", url=url)

    def extract_resources(self, ship_symbol: str, survey_full=None):  # type of survey_full?
        #    payload = {
        #       "survey": survey_full
        #    }
        url = f"{self.base_url}my/ships/{ship_symbol}/extract"
        if survey_full is None:
            return self.rate_limited(method="POST", url=url)
        else:
            raise NotImplementedError("survey_full as param for extract_resources not supported")
        #        return self.rate_limited(method="POST",url=url, json=payload).json())

    def jettison_cargo(self, ship_symbol: str, goods_symbol: str, units: int):
        payload = {
            "symbol": goods_symbol,
            "units": units
        }
        url = f"{self.base_url}my/ships/{ship_symbol}/jettison"
        return self.rate_limited(method="POST", url=url, json=payload)

    def jump_ship(self, ship_symbol: str, system_symbol: str):

        payload = {
            "systemSymbol": system_symbol
        }
        url = f"{self.base_url}my/ships/{ship_symbol}/jump"
        return self.rate_limited(method="POST", url=url, json=payload)

    def navigate_ship(self, ship_symbol: str, waypoint_symbol: str):
        payload = {
            "waypointSymbol": waypoint_symbol
        }
        url = f"{self.base_url}my/ships/{ship_symbol}/navigate"
        return self.rate_limited(method="POST", url=url, json=payload)

    def patch_ship_nav(self, ship_symbol: str, flight_mode: str):
        payload = {
            "flightMode": flight_mode
        }
        url = f"{self.base_url}my/ships/{ship_symbol}/nav"
        return self.rate_limited(method="PATCH", url=url, json=payload)

    def get_ship_nav(self, ship_symbol: str):
        url = f"{self.base_url}my/ships/{ship_symbol}/nav"
        return self.rate_limited(method="GET", url=url)

    def warp_ship(self, ship_symbol: str, waypoint_symbol: str):
        payload = {
            "waypointSymbol": waypoint_symbol
        }
        url = f"{self.base_url}my/ships/{ship_symbol}/warp"
        return self.rate_limited(method="POST", url=url, json=payload)

    def sell_cargo(self, ship_symbol: str, goods_symbol: str, units: str):
        payload = {
            "symbol": goods_symbol,
            "units": int(units)
        }
        url = f"{self.base_url}my/ships/{ship_symbol}/sell"
        return self.rate_limited(method="POST", url=url, json=payload)

    def scan_system(self, ship_symbol: str):
        url = f"{self.base_url}my/ships/{ship_symbol}/scan/systems"
        return self.rate_limited(method="POST", url=url)

    def scan_waypoint(self, ship_symbol: str):
        url = f"{self.base_url}my/ships/{ship_symbol}/scan/waypoints"
        return self.rate_limited(method="POST", url=url)

    def refuel_ship(self, ship_symbol: str, units: int):
        payload = {
            "units": units
        }
        url = f"{self.base_url}my/ships/{ship_symbol}/refuel"
        return self.rate_limited(method="POST", url=url, json=payload)

    def purchase_cargo(self, ship_symbol: str, goods_symbol: str, units: int):
        payload = {
            "symbol": goods_symbol,
            "units": units
        }
        url = f"{self.base_url}my/ships/{ship_symbol}/purchase"
        return self.rate_limited(method="POST", url=url, json=payload)

    def transfer_cargo(self, ship_symbol: str, goods_symbol: str, units: int, ship_symbol_target: str):
        payload = {
            "symbol": goods_symbol,
            "units": units,
            "shipSymbol": ship_symbol_target
        }
        url = f"{self.base_url}my/ships/{ship_symbol}/transfer"
        return self.rate_limited(method="POST", url=url, json=payload)

    def negotiate_contract(self, ship_symbol: str):
        url = f"{self.base_url}my/ships/{ship_symbol}/negotiate/contract"
        return self.rate_limited(method="POST", url=url)

    def get_mounts(self, ship_symbol: str):
        url = f"{self.base_url}my/ships/{ship_symbol}/mounts"
        return self.rate_limited(method="GET", url=url)

    def install_mount(self, ship_symbol: str, mount_symbol: str):
        payload = {
            "symbol": mount_symbol,
        }
        url = f"{self.base_url}my/ships/{ship_symbol}/mounts/install"
        return self.rate_limited(method="POST", url=url, json=payload)

    def remove_mount(self, ship_symbol: str, mount_symbol: str):
        payload = {
            "symbol": mount_symbol,
        }
        url = f"{self.base_url}my/ships/{ship_symbol}/mounts/remove"
        return self.rate_limited(method="POST", url=url, json=payload)

    def list_system(self, page: int = 1, limit: int = 10):
        parameters = {"page": page, "limit": limit}
        url = f"{self.base_url}systems"
        return self.rate_limited(method="GET", url=url, params=parameters)

    def get_system(self, system_symbol: str):
        url = f"{self.base_url}systems/{system_symbol}"
        return self.rate_limited(method="GET", url=url)

    def list_waypoints(self, system_symbol: str, page: int = 1, limit: int = 10):
        parameters = {"page": page, "limit": limit}
        url = f"{self.base_url}systems/{system_symbol}/waypoints"
        return self.rate_limited(method="GET", url=url, params=parameters)

    def get_waypoint(self, system_symbol: str, waypoint_symbol: str):
        url = f"{self.base_url}systems/{system_symbol}/waypoints/{waypoint_symbol}"
        return self.rate_limited(method="GET", url=url)

    def get_market(self, system_symbol: str, waypoint_symbol: str):
        url = f"{self.base_url}systems/{system_symbol}/waypoints/{waypoint_symbol}/market"
        return self.rate_limited(method="GET", url=url)

    def get_shipyard(self, system_symbol: str, waypoint_symbol: str):
        url = f"{self.base_url}systems/{system_symbol}/waypoints/{waypoint_symbol}/shipyard"
        return self.rate_limited(method="GET", url=url)

    def get_jump_gate(self, system_symbol: str, waypoint_symbol: str):
        url = f"{self.base_url}systems/{system_symbol}/waypoints/{waypoint_symbol}/jump-gate"
        return self.rate_limited(method="GET", url=url)
