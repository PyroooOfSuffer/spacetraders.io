response = [{
    "symbol": "string",
    "registration": {
        "name": "string",
        "factionSymbol": "string",
        "role": "FABRICATOR"
    },
    "nav": {
        "systemSymbol": "string",
        "waypointSymbol": "string",
        "route": {
            "destination": {
                "symbol": "string",
                "type": "PLANET",
                "systemSymbol": "string",
                "x": 0,
                "y": 0
            },
            "departure": {
                "symbol": "string",
                "type": "PLANET",
                "systemSymbol": "string",
                "x": 0,
                "y": 0
            },
            "departureTime": "2019-08-24T14:15:22Z",
            "arrival": "2019-08-24T14:15:22Z"
        },
        "status": "IN_TRANSIT",
        "flightMode": "CRUISE"
    },
    "crew": {
        "current": 0,
        "required": 0,
        "capacity": 0,
        "rotation": "STRICT",
        "morale": 0,
        "wages": 0
    },
    "frame": {
        "symbol": "FRAME_PROBE",
        "name": "string",
        "description": "string",
        "condition": 0,
        "moduleSlots": 0,
        "mountingPoints": 0,
        "fuelCapacity": 0,
        "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
        }
    },
    "reactor": {
        "symbol": "REACTOR_SOLAR_I",
        "name": "string",
        "description": "string",
        "condition": 0,
        "powerOutput": 1,
        "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
        }
    },
    "engine": {
        "symbol": "ENGINE_IMPULSE_DRIVE_I",
        "name": "string",
        "description": "string",
        "condition": 0,
        "speed": 1,
        "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
        }
    },
    "modules": [
        {
            "symbol": "MODULE_MINERAL_PROCESSOR_I",
            "capacity": 0,
            "range": 0,
            "name": "string",
            "description": "string",
            "requirements": {
                "power": 0,
                "crew": 0,
                "slots": 0
            }
        }
    ],
    "mounts": [
        {
            "symbol": "MOUNT_GAS_SIPHON_I",
            "name": "string",
            "description": "string",
            "strength": 0,
            "deposits": [
                "QUARTZ_SAND"
            ],
            "requirements": {
                "power": 0,
                "crew": 0,
                "slots": 0
            }
        }
    ],
    "cargo": {
        "capacity": 0,
        "units": 0,
        "inventory": [
            {
                "symbol": "string",
                "name": "string",
                "description": "string",
                "units": 1
            }
        ]
    },
    "fuel": {
        "current": 0,
        "capacity": 0,
        "consumed": {
            "amount": 0,
            "timestamp": "2019-08-24T14:15:22Z"
        }
    }
}]
