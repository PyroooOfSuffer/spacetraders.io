import requests
import time
import os


def get_token():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "auth_token.txt")

    with open(file_path, "r") as file:
        file_content = file.read()
        return file_content


auth_token = get_token()
session = requests.session()
session.base_url = "https://api.spacetraders.io/v2/"
headers = {'Authorization': 'Bearer ' + auth_token, 'Accept': 'application/json'}
session.headers = headers


def queue(result):
    ratelim = 0.5
    time.sleep(ratelim)
    return result


def create_new(symbol, faction, email):
    """
    Create a new Agent

    Parameters:
        symbol (str): Your desired agent symbol.
        faction (str): The symbol of the faction.
        email (str): Your Email address.

    Returns:
        dict: My Agent information plus token!
    """
    payload = {
        "symbol": symbol,
        "faction": faction,
        "email": email
    }
    return queue(requests.post("https://api.spacetraders.io/v2/register", json=payload).json())


def get_status():
    """
    Get the status of the SpaceTraders API.

    Returns:
        dict: API status information.
    """
    return queue(session.get(session.base_url).json())


def get_my_agent():
    """
    Get my agent information.

    Returns:
        dict: My agent information.
    """
    return queue(session.get(session.base_url + "my/agent").json())


def list_agent(page=1, lim=10):
    """
    List agent.

    Parameter:
        page (int): Page Nr.
        lim (int): Limit per Page

    Returns:
        dict: List of agent.
    """
    querystring = {"page": int(page), "limit": int(lim)}
    return queue(session.get(session.base_url + "/agents", params=querystring).json())


def get_agent(agent_symbol):
    """
    Retrieve detailed information about an agent using its symbol.

    Parameters:
        agent_symbol (str): Symbol of the agent.

    Returns:
        dict: Detailed agent information.
    """
    return queue(session.get(session.base_url + "/agents/" + agent_symbol).json())


def list_contracts(page=1, lim=10):
    """
    List contracts with optional pagination.

    Parameters:
        page (int): Page number for pagination (default is 1).
        lim (int): Limit of contracts per page (default is 10).

    Returns:
        dict: List of contracts based on pagination settings.
    """
    querystring = {"page": int(page), "limit": int(lim)}
    return queue(session.get(session.base_url + "/my/contracts", params=querystring).json())


def get_contract(contract_id):
    """
    Retrieve detailed information about a contract using its ID.

    Parameters:
        contract_id (str): ID of the contract.

    Returns:
        dict: Detailed contract information.
    """
    return queue(session.get(session.base_url + "/my/contracts/" + contract_id).json())


def accept_contract(contract_id):
    """
    Accept a contract by its ID.

    Parameters:
        contract_id (str): The ID of the contract to be accepted.

    Returns:
        dict: Result of the contract acceptance.
    """
    return queue(session.post(session.base_url + "/my/contracts/" + contract_id + "/accept").json())


def deliver_cargo_to_contract(contract_id, ship_symbol, trade_symbol, units):
    """
    Deliver cargo to fulfill a contract.

    Parameters:
        contract_id (str): The ID of the contract to fulfill.
        ship_symbol (str): Symbol of the ship carrying the cargo.
        trade_symbol (str): Symbol of the trade good to deliver.
        units (int): Number of units of the trade good to deliver.

    Returns:
        dict: Result of the cargo delivery operation.
    """
    payload = {
        "shipSymbol": ship_symbol,
        "tradeSymbol": trade_symbol,
        "units": int(units)
    }
    return queue(session.post(session.base_url + "/my/contracts/" + contract_id + "/deliver", json=payload).json())


def fulfill_contract(contract_id):
    """
    Fulfill a contract by its ID.

    Parameters:
        contract_id (str): The ID of the contract to be fulfilled.

    Returns:
        dict: Result of the contract fulfillment operation.
    """
    return queue(session.post(session.base_url + "/my/contracts/" + contract_id + "/fulfill").json())


def list_faction(page=1, lim=10):
    """
    List factions with optional pagination.

    Parameters:
        page (int): Page number for pagination (default is 1).
        lim (int): Limit of factions per page (default is 10).

    Returns:
        dict: List of factions according to the specified page and limit.
    """
    querystring = {"page": int(page), "limit": int(lim)}
    return queue(session.get(session.base_url + "/factions", params=querystring).json())


def get_faction(faction_symbol):
    """
    Retrieve detailed information about a faction using its symbol.

    Parameters:
        faction_symbol (str): Symbol of the faction to retrieve information for.

    Returns:
        dict: A dictionary containing detailed information about the specified faction.
    """
    return queue(session.get(session.base_url + "/factions/" + faction_symbol).json())


def list_ships(page=1, lim=10):
    """
    List ships with optional pagination.

    Parameters:
        page (int): Page number for pagination (default is 1).
        lim (int): Limit of ships per page (default is 10).

    Returns:
        dict: List of ships according to the specified page and limit.
    """
    querystring = {"page": int(page), "limit": int(lim)}
    return queue(session.get(session.base_url + "/my/ships", params=querystring).json())


def purchase_ship(ship_type, waypoint_symbol):
    """
    Purchase a new ship of the specified type.

    Parameters:
        ship_type (str): Type of the ship to be purchased.
        waypoint_symbol (str): Symbol of the waypoint where the ship will be purchased.

    Returns:
        dict: Result of the ship purchase operation.
    """
    payload = {
        "shipType": ship_type,
        "waypointSymbol": waypoint_symbol
    }
    return queue(session.post(session.base_url + "/my/ships", json=payload).json())


def get_ship(ship_symbol):
    """
    Retrieve detailed information about a ship using its symbol.

    Parameters:
        ship_symbol (str): Symbol of the ship to retrieve information for.

    Returns:
        dict: A dictionary containing detailed information about the specified ship.
    """
    return queue(session.get(session.base_url + "/my/ships/" + ship_symbol).json())


def get_ship_cargo(ship_symbol):
    """
    Retrieve cargo information of a ship using its symbol.

    Parameters:
        ship_symbol (str): Symbol of the ship to retrieve cargo information for.

    Returns:
        dict: A dictionary containing information about the cargo carried by the specified ship.
    """
    return queue(session.get(session.base_url + "/my/ships/" + ship_symbol + "/cargo").json())


def orbit_ship(ship_symbol):
    """
    Command a ship to enter orbit.

    Parameters:
        ship_symbol (str): Symbol of the ship to be commanded into orbit.

    Returns:
        dict: Result of the orbit command operation.
    """
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/orbit").json())


def ship_refine(ship_symbol, produce):
    """
    Refine cargo using a ship's refinery module.

    Parameters:
        ship_symbol (str): Symbol of the ship with a refinery module.
        produce (str): The type of cargo to be refined.

    Returns:
        dict: Result of the cargo refinement operation.
    """
    payload = {
        "produce": produce
    }
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/refine", json=payload).json())


def create_chart(ship_symbol):
    """
    Create a navigational chart for a ship.

    Parameters:
        ship_symbol (str): Symbol of the ship to create a navigational chart for.

    Returns:
        dict: Result of the navigational chart creation operation.
    """
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/chart").json())


def get_ship_cooldown(ship_symbol):
    """
    Retrieve cooldown information for a ship.

    Parameters:
        ship_symbol (str): Symbol of the ship to retrieve cooldown information for.

    Returns:
        dict: A dictionary containing information about the current cooldown affecting the specified ship.
    """
    return queue(session.get(session.base_url + "/my/ships/" + ship_symbol + "/cooldown").json())


def dock_ship(ship_symbol):
    """
    Command a ship to dock at a station.

    Parameters:
        ship_symbol (str): Symbol of the ship to be commanded to dock.

    Returns:
        dict: Result of the dock command operation.
    """
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/dock").json())


def create_survey(ship_symbol):
    """
    Initiate a resource survey using a ship.

    Parameters:
        ship_symbol (str): Symbol of the ship to initiate the resource survey.

    Returns:
        dict: Result of the resource survey initiation operation.
    """
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/survey").json())


def extract_resources(ship_symbol, survey_full=None):  # will need FIXING
    """
    Extract resources from a location using a ship's survey data.

    Parameters:
        ship_symbol (str): Symbol of the ship used to extract resources.
        survey_full (dict): Survey data used for resource extraction. If provided, the extraction will be based on this survey data.

    Returns:
        dict: Result of the resource extraction operation.
    """
    #    payload = {
    #       "survey": survey_full
    #    }
    if survey_full is None:
        return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/extract").json())
    else:
        raise NotImplementedError("survey_full as param for extract_resources not supported")
    #        return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/extract", json=payload).json())


def jettison_cargo(ship_symbol, goods_symbol, units):
    """
    Jettison cargo from a ship.

    Parameters:
        ship_symbol (str): Symbol of the ship from which to jettison cargo.
        goods_symbol (str): Symbol of the type of cargo to jettison.
        units (int): Number of units of cargo to jettison.

    Returns:
        dict: Result of the cargo jettison operation.
    """
    payload = {
        "symbol": goods_symbol,
        "units": int(units)
    }
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/jettison", json=payload).json())


def jump_ship(ship_symbol, system_symbol):
    """
    Initiate a jump to another system using a ship's jump drive.

    Parameters:
        ship_symbol (str): Symbol of the ship to initiate the jump.
        system_symbol (str): Symbol of the target system to jump to.

    Returns:
        dict: Result of the jump initiation operation.
    """
    payload = {
        "systemSymbol": system_symbol
    }
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/jump", json=payload).json())


def navigate_ship(ship_symbol, waypoint_symbol):
    """
    Navigate a ship to a specific waypoint.

    Parameters:
        ship_symbol (str): Symbol of the ship to navigate.
        waypoint_symbol (str): Symbol of the target waypoint to navigate to.

    Returns:
        dict: Result of the navigation operation.
    """
    payload = {
        "waypointSymbol": waypoint_symbol
    }
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/navigate", json=payload).json())


def patch_ship_nav(ship_symbol, flight_mode):
    """
    Update the navigation settings of a ship.

    Parameters:
        ship_symbol (str): Symbol of the ship to update the navigation settings for.
        flight_mode (str): Desired flight mode for the ship's navigation.

    Returns:
        dict: Result of the navigation settings update operation.
    """
    payload = {
        "flightMode": flight_mode
    }
    return queue(session.patch(session.base_url + "/my/ships/" + ship_symbol + "/nav", json=payload).json())


def get_ship_nav(ship_symbol):
    """
    Retrieve navigation settings of a ship.

    Parameters:
        ship_symbol (str): Symbol of the ship to retrieve navigation settings for.

    Returns:
        dict: A dictionary containing the navigation settings of the specified ship.
    """
    return queue(session.get(session.base_url + "/my/ships/" + ship_symbol + "/nav").json())


def warp_ship(ship_symbol, waypoint_symbol):
    """
    Initiate a warp jump using a ship's warp drive.

    Parameters:
        ship_symbol (str): Symbol of the ship to initiate the warp jump.
        waypoint_symbol (str): Symbol of the target waypoint to warp to.

    Returns:
        dict: Result of the warp jump initiation operation.
    """
    payload = {
        "waypointSymbol": waypoint_symbol
    }
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/warp", json=payload).json())


def sell_cargo(ship_symbol, goods_symbol, units):
    """
    Sell cargo from a ship to a marketplace.

    Parameters:
        ship_symbol (str): Symbol of the ship from which to sell cargo.
        goods_symbol (str): Symbol of the type of cargo to sell.
        units (int): Number of units of cargo to sell.

    Returns:
        dict: Result of the cargo selling operation.
    """
    payload = {
        "symbol": goods_symbol,
        "units": int(units)
    }
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/sell", json=payload).json())


def scan_system(ship_symbol):
    """
    Perform a system scan using a ship's scanning equipment.

    Parameters:
        ship_symbol (str): Symbol of the ship to perform the system scan.

    Returns:
        dict: Result of the system scan operation.
    """
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/scan/systems").json())


def scan_waypoint(ship_symbol):
    """
    Perform a waypoint scan using a ship's scanning equipment.

    Parameters:
        ship_symbol (str): Symbol of the ship to perform the waypoint scan.

    Returns:
        dict: Result of the waypoint scan operation.
    """
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/scan/waypoints").json())


def refuel_ship(ship_symbol, units):
    """
    Refuel a ship using available resources.

    Parameters:
        ship_symbol (str): Symbol of the ship to refuel.
        units (int): Number of units to use for refueling.

    Returns:
        dict: Result of the ship refueling operation.
    """
    payload = {
        "units": int(units)
    }
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/refuel", json=payload).json())


def purchase_cargo(ship_symbol, goods_symbol, units):
    """
    Purchase cargo for a ship from a marketplace.

    Parameters:
        ship_symbol (str): Symbol of the ship for which to purchase cargo.
        goods_symbol (str): Symbol of the type of cargo to purchase.
        units (int): Number of units of cargo to purchase.

    Returns:
        dict: Result of the cargo purchase operation.
    """
    payload = {
        "symbol": goods_symbol,
        "units": int(units)
    }
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/purchase", json=payload).json())


def transfer_cargo(ship_symbol, goods_symbol, units, ship_symbol_target):
    """
    Transfer cargo between two ships.

    Parameters:
        ship_symbol (str): Symbol of the source ship from which to transfer cargo.
        goods_symbol (str): Symbol of the type of cargo to transfer.
        units (int): Number of units of cargo to transfer.
        ship_symbol_target (str): Symbol of the target ship to which cargo should be transferred.

    Returns:
        dict: Result of the cargo transfer operation.
    """
    payload = {
        "symbol": goods_symbol,
        "units": int(units),
        "shipSymbol": ship_symbol_target
    }
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/transfer", json=payload).json())


def negotiate_contract(ship_symbol):
    """
    Initiate negotiations for a new contract.

    Parameters:
        ship_symbol (str): Symbol of the ship to initiate contract negotiations.

    Returns:
        dict: Result of the contract negotiation initiation.
    """
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/negotiate/contract").json())


def get_mounts(ship_symbol):
    """
    Retrieve information about mounts on a ship.

    Parameters:
        ship_symbol (str): Symbol of the ship to retrieve mount information.

    Returns:
        dict: Information about the mounts on the ship.
    """
    return queue(session.get(session.base_url + "/my/ships/" + ship_symbol + "/mounts").json())


def install_mount(ship_symbol, mount_symbol):
    """
    Install a module on a ship's mount.

    Parameters:
        ship_symbol (str): Symbol of the ship on which to install the module.
        mount_symbol (str): Symbol of the module to be installed.

    Returns:
        dict: Result of the module installation operation.
    """
    payload = {
        "symbol": mount_symbol,
    }
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/mounts/install", json=payload).json())


def remove_mount(ship_symbol, mount_symbol):
    """
    Remove a module from a ship's mount.

    Parameters:
        ship_symbol (str): Symbol of the ship from which to remove the module.
        mount_symbol (str): Symbol of the module to be removed.

    Returns:
        dict: Result of the module removal operation.
    """
    payload = {
        "symbol": mount_symbol,
    }
    return queue(session.post(session.base_url + "/my/ships/" + ship_symbol + "/mounts/remove", json=payload).json())


def list_system(page=1, lim=10):
    """
    List systems in the SpaceTraders universe.

    Parameters:
        page (int): Page number of the system list (default is 1).
        lim (int): Limit of systems per page (default is 10).

    Returns:
        dict: List of systems with pagination information.
    """
    querystring = {"page": int(page), "limit": int(lim)}
    return queue(session.get(session.base_url + "/systems", params=querystring).json())


def get_system(system_symbol):
    """
    Get detailed information about a specific system.

    Parameters:
        system_symbol (str): Symbol of the system for which to retrieve information.

    Returns:
        dict: Detailed information about the specified system.
    """
    return queue(session.get(session.base_url + "/systems/" + system_symbol).json())


def list_waypoints(system_symbol, page=1, lim=10):
    """
    List waypoints within a specific system.

    Parameters:
        system_symbol (str): Symbol of the system for which to list waypoints.
        page (int): Page number of the waypoint list (default is 1).
        lim (int): Limit of waypoints per page (default is 10).

    Returns:
        dict: List of waypoints within the specified system with pagination information.
    """
    querystring = {"page": int(page), "limit": int(lim)}
    return queue(session.get(session.base_url + "/systems/" + system_symbol + "/waypoints", params=querystring).json())


def get_waypoint(system_symbol, waypoint_symbol):
    """
    Get detailed information about a specific waypoint within a system.

    Parameters:
        system_symbol (str): Symbol of the system containing the waypoint.
        waypoint_symbol (str): Symbol of the waypoint for which to retrieve information.

    Returns:
        dict: Detailed information about the specified waypoint.
    """
    return queue(session.get(session.base_url + "/systems/" + system_symbol + "/waypoints/" + waypoint_symbol).json())


def get_market(system_symbol, waypoint_symbol):
    """
    Get market information for a specific waypoint within a system.

    Parameters:
        system_symbol (str): Symbol of the system containing the waypoint.
        waypoint_symbol (str): Symbol of the waypoint for which to retrieve market information.

    Returns:
        dict: Market information for the specified waypoint.
    """
    return queue(session.get(
        session.base_url + "/systems/" + system_symbol + "/waypoints/" + waypoint_symbol + "/market").json())


def get_shipyard(system_symbol, waypoint_symbol):
    """
    Get shipyard information for a specific waypoint within a system.

    Parameters:
        system_symbol (str): Symbol of the system containing the waypoint.
        waypoint_symbol (str): Symbol of the waypoint for which to retrieve shipyard information.

    Returns:
        dict: Shipyard information for the specified waypoint.
    """
    return queue(session.get(
        session.base_url + "/systems/" + system_symbol + "/waypoints/" + waypoint_symbol + "/shipyard").json())


def get_jump_gate(system_symbol, waypoint_symbol):
    """
    Get information about a jump gate at a specific waypoint within a system.

    Parameters:
        system_symbol (str): Symbol of the system containing the waypoint with the jump gate.
        waypoint_symbol (str): Symbol of the waypoint with the jump gate for which to retrieve information.

    Returns:
        dict: Information about the jump gate at the specified waypoint.
    """
    return queue(session.get(
        session.base_url + "/systems/" + system_symbol + "/waypoints/" + waypoint_symbol + "/jump-gate").json())
