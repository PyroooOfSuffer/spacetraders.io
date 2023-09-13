ship_list_data = [
    {
        "symbol": "PYROOO-1",
        "nav": {
            "systemSymbol": "X1-GX37",
            "waypointSymbol": "X1-GX37-27130X",
            "route": {
                "departure": {
                    "symbol": "X1-GX37-27130X",
                    "type": "PLANET",
                    "systemSymbol": "X1-GX37",
                    "x": -20,
                    "y": -14
                },
                "destination": {
                    "symbol": "X1-GX37-27130X",
                    "type": "PLANET",
                    "systemSymbol": "X1-GX37",
                    "x": -20,
                    "y": -14
                },
                "arrival": "2023-09-10T17:30:07.056Z",
                "departureTime": "2023-09-10T17:30:07.056Z"
            },
            "status": "DOCKED",
            "flightMode": "CRUISE"
        },
        "crew": {
            "current": 59,
            "capacity": 80,
            "required": 59,
            "rotation": "STRICT",
            "morale": 100,
            "wages": 0
        },
        "fuel": {
            "current": 1200,
            "capacity": 1200,
            "consumed": {
                "amount": 0,
                "timestamp": "2023-09-10T17:30:07.056Z"
            }
        },
        "frame": {
            "symbol": "FRAME_FRIGATE",
            "name": "Frame Frigate",
            "description": "A medium-sized, multi-purpose spacecraft, often used for combat, transport, or support operations.",
            "moduleSlots": 8,
            "mountingPoints": 5,
            "fuelCapacity": 1200,
            "condition": 100,
            "requirements": {
                "power": 8,
                "crew": 25
            }
        },
        "reactor": {
            "symbol": "REACTOR_FISSION_I",
            "name": "Fission Reactor I",
            "description": "A basic fission power reactor, used to generate electricity from nuclear fission reactions.",
            "condition": 100,
            "powerOutput": 31,
            "requirements": {
                "crew": 8
            }
        },
        "engine": {
            "symbol": "ENGINE_ION_DRIVE_II",
            "name": "Ion Drive II",
            "description": "An advanced propulsion system that uses ionized particles to generate high-speed, low-thrust acceleration, with improved efficiency and performance.",
            "condition": 100,
            "speed": 30,
            "requirements": {
                "power": 6,
                "crew": 8
            }
        },
        "modules": [
            {
                "symbol": "MODULE_CARGO_HOLD_I",
                "name": "Cargo Hold",
                "description": "A module that increases a ship's cargo capacity.",
                "capacity": 30,
                "requirements": {
                    "crew": 0,
                    "power": 1,
                    "slots": 1
                }
            },
            {
                "symbol": "MODULE_CARGO_HOLD_I",
                "name": "Cargo Hold",
                "description": "A module that increases a ship's cargo capacity.",
                "capacity": 30,
                "requirements": {
                    "crew": 0,
                    "power": 1,
                    "slots": 1
                }
            },
            {
                "symbol": "MODULE_CREW_QUARTERS_I",
                "name": "Crew Quarters",
                "description": "A module that provides living space and amenities for the crew.",
                "capacity": 40,
                "requirements": {
                    "crew": 2,
                    "power": 1,
                    "slots": 1
                }
            },
            {
                "symbol": "MODULE_CREW_QUARTERS_I",
                "name": "Crew Quarters",
                "description": "A module that provides living space and amenities for the crew.",
                "capacity": 40,
                "requirements": {
                    "crew": 2,
                    "power": 1,
                    "slots": 1
                }
            },
            {
                "symbol": "MODULE_MINERAL_PROCESSOR_I",
                "name": "Mineral Processor",
                "description": "Crushes and processes extracted minerals and ores into their component parts, filters out impurities, and containerizes them into raw storage units.",
                "requirements": {
                    "crew": 0,
                    "power": 1,
                    "slots": 2
                }
            },
            {
                "symbol": "MODULE_JUMP_DRIVE_I",
                "name": "Jump Drive I",
                "description": "A basic antimatter jump drive that allows for instantaneous short-range interdimensional travel.",
                "range": 500,
                "requirements": {
                    "crew": 10,
                    "power": 4,
                    "slots": 1
                }
            },
            {
                "symbol": "MODULE_WARP_DRIVE_I",
                "name": "Warp Drive I",
                "description": "A basic warp drive that allows for short-range interstellar travel.",
                "range": 2000,
                "requirements": {
                    "crew": 2,
                    "power": 3,
                    "slots": 1
                }
            }
        ],
        "mounts": [
            {
                "symbol": "MOUNT_SENSOR_ARRAY_I",
                "name": "Sensor Array I",
                "description": "A basic sensor array that improves a ship's ability to detect and track other objects in space.",
                "strength": 1,
                "requirements": {
                    "crew": 0,
                    "power": 1
                }
            },
            {
                "symbol": "MOUNT_MINING_LASER_I",
                "name": "Mining Laser I",
                "description": "A basic mining laser that can be used to extract valuable minerals from asteroids and other space objects.",
                "strength": 10,
                "requirements": {
                    "crew": 0,
                    "power": 1
                }
            },
            {
                "symbol": "MOUNT_SURVEYOR_I",
                "name": "Surveyor I",
                "description": "A basic survey probe that can be used to gather information about a mineral deposit.",
                "strength": 1,
                "deposits": [
                    "QUARTZ_SAND",
                    "SILICON_CRYSTALS",
                    "PRECIOUS_STONES",
                    "ICE_WATER",
                    "AMMONIA_ICE",
                    "IRON_ORE",
                    "COPPER_ORE",
                    "SILVER_ORE",
                    "ALUMINUM_ORE",
                    "GOLD_ORE",
                    "PLATINUM_ORE"
                ],
                "requirements": {
                    "crew": 2,
                    "power": 1
                }
            }
        ],
        "registration": {
            "name": "PYROOO-1",
            "factionSymbol": "COSMIC",
            "role": "COMMAND"
        },
        "cargo": {
            "capacity": 60,
            "units": 0,
            "inventory": [

            ]
        }
    },

    {
        "symbol": "PYROOO-2",
        "nav": {
            "systemSymbol": "X1-GX37",
            "waypointSymbol": "X1-GX37-48697D",
            "route": {
                "departure": {
                    "symbol": "X1-GX37-48697D",
                    "type": "ORBITAL_STATION",
                    "systemSymbol": "X1-GX37",
                    "x": 23,
                    "y": -49
                },
                "destination": {
                    "symbol": "X1-GX37-48697D",
                    "type": "ORBITAL_STATION",
                    "systemSymbol": "X1-GX37",
                    "x": 23,
                    "y": -49
                },
                "arrival": "2023-09-10T17:30:07.144Z",
                "departureTime": "2023-09-10T17:30:07.144Z"
            },
            "status": "DOCKED",
            "flightMode": "CRUISE"
        },
        "crew": {
            "current": 0,
            "capacity": 0,
            "required": 0,
            "rotation": "STRICT",
            "morale": 100,
            "wages": 0
        },
        "fuel": {
            "current": 0,
            "capacity": 0,
            "consumed": {
                "amount": 0,
                "timestamp": "2023-09-10T17:30:07.144Z"
            }
        },
        "frame": {
            "symbol": "FRAME_PROBE",
            "name": "Frame Probe",
            "description": "A small, unmanned spacecraft used for exploration, reconnaissance, and scientific research.",
            "moduleSlots": 0,
            "mountingPoints": 0,
            "fuelCapacity": 0,
            "condition": 100,
            "requirements": {
                "power": 1,
                "crew": 0
            }
        },
        "reactor": {
            "symbol": "REACTOR_SOLAR_I",
            "name": "Solar Reactor I",
            "description": "A basic solar power reactor, used to generate electricity from solar energy.",
            "condition": 100,
            "powerOutput": 3,
            "requirements": {
                "crew": 0
            }
        },
        "engine": {
            "symbol": "ENGINE_IMPULSE_DRIVE_I",
            "name": "Impulse Drive I",
            "description": "A basic low-energy propulsion system that generates thrust for interplanetary travel.",
            "condition": 100,
            "speed": 2,
            "requirements": {
                "power": 1,
                "crew": 0
            }
        },
        "modules": [

        ],
        "mounts": [

        ],
        "registration": {
            "name": "PYROOO-2",
            "factionSymbol": "COSMIC",
            "role": "SATELLITE"
        },
        "cargo": {
            "capacity": 0,
            "units": 0,
            "inventory": [

            ]
        }
    }
]

agent_list_data = [
    {
        'symbol': '00D5Z8PD1NIEXZ',
        'headquarters': 'X1-GX37-27130X',
        'credits': 59559,
        'startingFaction': 'COSMIC',
        'shipCount': 3
    },
    {
        'symbol': '01HQISG27JL8C0',
        'headquarters': 'X1-GX37-27130X',
        'credits': 63836,
        'startingFaction': 'COSMIC',
        'shipCount': 3
    }
]

contract_list_data = [
    {
        'id': 'clmdqd9vgey1cs60cbc89n2yt',
        'factionSymbol': 'COSMIC',
        'type': 'PROCUREMENT',
        'terms': {
            'deadline': '2023-09-17T17:30:07.021Z',
            'payment': {
                'onAccepted': 31842,
                'onFulfilled': 155916
            },
            'deliver': [
                {
                    'tradeSymbol': 'COPPER_ORE',
                    'destinationSymbol': 'X1-GX37-12642E',
                    'unitsRequired': 1220,
                    'unitsFulfilled': 0
                }
            ]
        },
        'accepted': False,
        'fulfilled': False,
        'expiration': '2023-09-11T17:30:07.021Z',
        'deadlineToAccept': '2023-09-11T17:30:07.021Z'
    }
]

faction_list_data = [
    {
        "symbol": "COSMIC",
        "name": "Cosmic Engineers",
        "description": "The Cosmic Engineers are a group of highly advanced scientists and engineers who seek to terraform and colonize new worlds, pushing the boundaries of technology and exploration.",
        "headquarters": "X1-GX37-27130X",
        "traits": [
            {
                "symbol": "INNOVATIVE",
                "name": "Innovative",
                "description": "Willing to try new and untested ideas. Sometimes able to come up with creative and original solutions to problems, and may be able to think outside the box. Sometimes at the forefront of technological or social change, and may be willing to take risks in order to advance the boundaries of human knowledge and understanding."
            },
            {
                "symbol": "BOLD",
                "name": "Bold",
                "description": "Unafraid to take risks and challenge the status quo. Sometimes willing to do things that others would not dare, and may be able to overcome obstacles and challenges that would be insurmountable for others. Sometimes able to inspire and motivate others to take bold action as well."
            },
            {
                "symbol": "VISIONARY",
                "name": "Visionary",
                "description": "Possessing a clear and compelling vision for the future. Sometimes able to see beyond the present and anticipate the needs and challenges of tomorrow. Sometimes able to inspire and guide others towards a better and brighter future, and may be willing to take bold and decisive action to make their vision a reality."
            },
            {
                "symbol": "CURIOUS",
                "name": "Curious",
                "description": "Possessing a strong desire to learn and explore. Sometimes interested in a wide range of topics and may be willing to take risks in order to satisfy their curiosity. Sometimes able to think outside the box and come up with creative solutions to challenges."
            }
        ],
        "isRecruiting": True
    },
    {
        "symbol": "VOID",
        "name": "Voidfarers",
        "description": "The Voidfarers are a group of nomadic traders and adventurers who travel the galaxy in search of riches and adventure, willing to take risks and explore the unknown.",
        "headquarters": "X1-KA2-14150X",
        "traits": [
            {
                "symbol": "DARING",
                "name": "Daring",
                "description": "Willing to take risks and challenges. Sometimes unafraid to explore new and unknown territories, and may be willing to take bold and decisive action in order to achieve their goals. Sometimes able to overcome challenges that would be insurmountable for others."
            },
            {
                "symbol": "EXPLORATORY",
                "name": "Exploratory",
                "description": "Dedicated to exploration and discovery. Sometimes interested in mapping new territories and uncovering the secrets of the universe. Sometimes able to overcome obstacles and challenges in order to advance the boundaries of human knowledge and understanding."
            },
            {
                "symbol": "RESOURCEFUL",
                "name": "Resourceful",
                "description": "Known for their ingenuity and ability to make the most out of limited resources. Able to improvise and adapt to changing circumstances, using whatever is available to them in order to overcome challenges and achieve their goals."
            },
            {
                "symbol": "FLEXIBLE",
                "name": "Flexible",
                "description": "Able to adapt to changing circumstances and environments. Sometimes able to quickly switch between different strategies and tactics in order to respond to new challenges or opportunities. Sometimes able to improvise and think on their feet, making them difficult to predict or outmaneuver."
            }
        ],
        "isRecruiting": True
    },
    {
        "symbol": "GALACTIC",
        "name": "Galactic Alliance",
        "description": "The Galactic Alliance is a coalition of planets and factions that have banded together for mutual protection and support, working together to defend against external threats and promote cooperation.",
        "headquarters": "X1-QZ57-68340B",
        "traits": [
            {
                "symbol": "COOPERATIVE",
                "name": "Cooperative",
                "description": "Willing to work together with others in order to achieve common goals. Sometimes able to coordinate and cooperate effectively, using their collective strengths and resources to overcome challenges and achieve success. Often prioritize collaboration and teamwork over individual achievement."
            },
            {
                "symbol": "UNITED",
                "name": "United",
                "description": "Strongly united and cohesive, often with a strong sense of shared identity and purpose. Sometimes able to work together effectively and efficiently, and may be difficult to divide or conquer. Sometimes able to overcome challenges that would be insurmountable for a less united group."
            },
            {
                "symbol": "PEACEFUL",
                "name": "Peaceful",
                "description": "Dedicated to maintaining peace and harmony. Sometimes reluctant to engage in conflict, and may prefer to resolve disputes through negotiation and diplomacy. Sometimes able to create a sense of community and belonging, and may be able to build strong and lasting relationships with others."
            },
            {
                "symbol": "STRATEGIC",
                "name": "Strategic",
                "description": "Skilled in the art of strategy and planning. Sometimes able to think ahead and anticipate the actions of others, and may be able to develop effective plans to achieve their goals. Sometimes able to make calculated risks and sacrifices in order to gain a strategic advantage."
            }
        ],
        "isRecruiting": True
    },
    {
        "symbol": "QUANTUM",
        "name": "Quantum Federation",
        "description": "The Quantum Federation is a group of planets and factions that have joined together to share knowledge and technology, using their collective expertise to advance the science and technology of the galaxy.",
        "headquarters": "X1-Z40-24820B",
        "traits": [
            {
                "symbol": "INTELLIGENT",
                "name": "Intelligent",
                "description": "Possessing a high level of intelligence and analytical ability. Sometimes skilled in a wide range of fields, including science, technology, and engineering. Often have a strong curiosity and a desire to understand the mysteries of the universe."
            },
            {
                "symbol": "RESEARCH_FOCUSED",
                "name": "Research-Focused",
                "description": "Dedicated to advancing knowledge and understanding through research and experimentation. Often have a strong focus on scientific and technological development, and may be willing to take risks and explore new ideas in order to make progress."
            },
            {
                "symbol": "COLLABORATIVE",
                "name": "Collaborative",
                "description": "Known for their ability to work well with others. Sometimes willing to share resources, knowledge, and expertise in order to achieve common goals. Often have a strong sense of community and cooperation, and may prioritize the needs of the group over those of the individual."
            },
            {
                "symbol": "PROGRESSIVE",
                "name": "Progressive",
                "description": "Open to new ideas and change. Sometimes willing to embrace new technologies and ways of thinking, and may prioritize the advancement of knowledge and understanding over tradition and established ways of doing things."
            }
        ],
        "isRecruiting": True
    },
    {
        "symbol": "DOMINION",
        "name": "Stellar Dominion",
        "description": "The Stellar Dominion is a powerful, expansionist faction that seeks to conquer and control as many systems as possible, using their advanced technology and military might to dominate their rivals.",
        "headquarters": "X1-HV75-10740C",
        "traits": [
            {
                "symbol": "MILITARISTIC",
                "name": "Militaristic",
                "description": "Focused on building and maintaining a strong military force. Often prioritize military power and readiness over other concerns, and may be quick to engage in conflict or aggression in order to achieve their goals."
            },
            {
                "symbol": "AGGRESSIVE",
                "name": "Aggressive",
                "description": "Quick to engage in conflict or aggression, often without provocation. Sometimes unpredictable and difficult to negotiate with, and may prioritize their own interests over the needs of others."
            },
            {
                "symbol": "IMPERIALISTIC",
                "name": "Imperialistic",
                "description": "Dedicated to expanding their territory and influence. Often seek to conquer or subjugate other factions, and may have a hierarchical and authoritarian structure. Often prioritize the interests of their own faction over the needs of others."
            },
            {
                "symbol": "INDUSTRIOUS",
                "name": "Industrious",
                "description": "Known for their hard work and dedication. Highly productive and efficient, with a focus on maximizing their output. Sometimes able to produce large quantities of goods or resources, but may also be vulnerable to exploitation or overwork."
            }
        ],
        "isRecruiting": True
    },
    {
        "symbol": "ASTRO",
        "name": "Astro-Salvage Alliance",
        "description": "The Astro-Salvage Alliance is a group of scavengers and salvagers who search the galaxy for ancient artifacts and valuable technology, often combing through old ship battlegrounds and derelict space stations.",
        "headquarters": "X1-PC31-44670Z",
        "traits": [
            {
                "symbol": "SCAVENGERS",
                "name": "Scavengers",
                "description": "Skilled at finding and salvaging valuable resources and materials from abandoned or derelict ships, space stations, and other structures. Resourceful and able to make the most out of what others have left behind."
            },
            {
                "symbol": "TREASURE_HUNTERS",
                "name": "Treasure Hunters",
                "description": "Always on the lookout for valuable artifacts, ancient relics, and other rare and valuable items. Curious and willing to take risks in order to uncover hidden treasures and secrets of the universe."
            },
            {
                "symbol": "RESOURCEFUL",
                "name": "Resourceful",
                "description": "Known for their ingenuity and ability to make the most out of limited resources. Able to improvise and adapt to changing circumstances, using whatever is available to them in order to overcome challenges and achieve their goals."
            },
            {
                "symbol": "DEXTEROUS",
                "name": "Dexterous",
                "description": "Skilled in the use of their hands and able to perform complex tasks with precision and accuracy. Known for their manual dexterity and ability to manipulate objects with ease, making them valuable in a wide range of tasks and activities."
            }
        ],
        "isRecruiting": True
    },
    {
        "symbol": "CORSAIRS",
        "name": "Seventh Space Corsairs",
        "description": "The Seventh Space Corsairs are a feared group of pirates and raiders who operate throughout the galaxy, preying on merchant ships and plundering valuable cargo.",
        "headquarters": "X1-ST77-58550Z",
        "traits": [
            {
                "symbol": "UNPREDICTABLE",
                "name": "Unpredictable",
                "description": "Difficult to predict or anticipate, with a tendency to act in unexpected or chaotic ways."
            },
            {
                "symbol": "BRUTAL",
                "name": "Brutal",
                "description": "Fierce and ruthless, with a willingness to use violence or intimidation to achieve their goals. Often feared or respected by others, but may also be viewed as a threat or enemy by those who oppose their methods."
            },
            {
                "symbol": "FLEETING",
                "name": "Fleeting",
                "description": "Not permanently settled in one place, with a tendency to move frequently or unpredictably. Sometimes difficult to find or track, but may also be able to take advantage of opportunities or evade threats by moving quickly or unexpectedly."
            },
            {
                "symbol": "ADAPTABLE",
                "name": "Adaptable",
                "description": "Quick to adapt to changing circumstances, with the ability to adjust their plans or strategies in response to new information or challenges. Sometimes able to thrive in a wide range of environments or situations, but may also be vulnerable to sudden or unexpected changes."
            }
        ],
        "isRecruiting": True
    },
    {
        "symbol": "OBSIDIAN",
        "name": "Obsidian Syndicate",
        "description": "The Obsidian Syndicate is a secretive and powerful organization, often involved in illicit activities. They have a vast network of informants and are known for their intelligence capabilities. Not much is known about their actual structure or aims, as they are a highly guarded faction.",
        "headquarters": "X1-AU89-67330F",
        "traits": [
            {
                "symbol": "SECRETIVE",
                "name": "Secretive",
                "description": "Guarded and secretive, with a tendency to keep their plans and activities hidden from others. Sometimes difficult to negotiate with or trust, but may have valuable information or resources that they are willing to share with the right partners."
            },
            {
                "symbol": "INTELLIGENT",
                "name": "Intelligent",
                "description": "Possessing a high level of intelligence and analytical ability. Sometimes skilled in a wide range of fields, including science, technology, and engineering. Often have a strong curiosity and a desire to understand the mysteries of the universe."
            },
            {
                "symbol": "SMUGGLERS",
                "name": "Smugglers",
                "description": "Skilled at moving goods or people across borders or through restricted areas. Sometimes able to avoid detection or interception, and may be able to find hidden or secret routes. Sometimes able to evade or bypass regulations or controls, and may be willing to engage in illegal or risky activities in order to achieve their goals."
            },
            {
                "symbol": "UNPREDICTABLE",
                "name": "Unpredictable",
                "description": "Difficult to predict or anticipate, with a tendency to act in unexpected or chaotic ways."
            }
        ],
        "isRecruiting": True
    },
    {
        "symbol": "AEGIS",
        "name": "Aegis Collective",
        "description": "The Aegis Collective is a group of fortified settlements united under a common goal: survival. They focus on defensive strategies and are known to be exceptionally self-sufficient. Despite their somewhat closed-off nature, they are always willing to take in those who need protection.",
        "headquarters": "X1-HR78-35460F",
        "traits": [
            {
                "symbol": "DEFENSIVE",
                "name": "Defensive",
                "description": "Prepared and able to defend themselves against potential threats. Often have strong military forces or defensive capabilities, but may also be vulnerable to surprise attacks or other forms of aggression."
            },
            {
                "symbol": "SELF_SUFFICIENT",
                "name": "Self-Sufficient",
                "description": "Able to sustain themselves without relying on others for support or resources. Sometimes independent and self-reliant, but may also be isolated or vulnerable to external threats."
            },
            {
                "symbol": "PROUD",
                "name": "Proud",
                "description": "Proud of their heritage, culture, or achievements, with a strong sense of identity and self-respect. Sometimes resistant to change or outside influence, and may be willing to defend their beliefs or values against challenges or threats."
            },
            {
                "symbol": "WELCOMING",
                "name": "Welcoming",
                "description": "Open and receptive to outsiders. Sometimes friendly and hospitable, and may be willing to extend a warm welcome to newcomers. Sometimes able to create a sense of community and belonging, and may be able to build strong and lasting relationships with others."
            }
        ],
        "isRecruiting": True
    },
    {
        "symbol": "UNITED",
        "name": "United Independent Settlements",
        "description": "The United Independent Settlements is a loose coalition of small settlements and outposts that have joined together for mutual support and protection, working to defend their independence against larger factions and protect their way of life.",
        "headquarters": "X1-NB2-20410C",
        "traits": [
            {
                "symbol": "SELF_SUFFICIENT",
                "name": "Self-Sufficient",
                "description": "Able to sustain themselves without relying on others for support or resources. Sometimes independent and self-reliant, but may also be isolated or vulnerable to external threats."
            },
            {
                "symbol": "DEFENSIVE",
                "name": "Defensive",
                "description": "Prepared and able to defend themselves against potential threats. Often have strong military forces or defensive capabilities, but may also be vulnerable to surprise attacks or other forms of aggression."
            },
            {
                "symbol": "PROUD",
                "name": "Proud",
                "description": "Proud of their heritage, culture, or achievements, with a strong sense of identity and self-respect. Sometimes resistant to change or outside influence, and may be willing to defend their beliefs or values against challenges or threats."
            },
            {
                "symbol": "DIVERSE",
                "name": "Diverse",
                "description": "Comprised of a diverse range of individuals, cultures, or beliefs. Sometimes able to offer a wide range of perspectives and expertise, but may also face challenges in achieving unity or consensus."
            }
        ],
        "isRecruiting": True
    }
]

symbol_list_data = [
    {
        "symbol": "X1-GX37",
        "sectorSymbol": "X1",
        "type": "BLUE_STAR",
        "x": -9896,
        "y": -9709,
        "waypoints": [
            {
                "symbol": "X1-GX37-79391X",
                "type": "PLANET",
                "x": -12,
                "y": -6
            },
            {
                "symbol": "X1-GX37-27130X",
                "type": "PLANET",
                "x": -20,
                "y": -14
            },
            {
                "symbol": "X1-GX37-12642E",
                "type": "MOON",
                "x": -20,
                "y": -14
            },
            {
                "symbol": "X1-GX37-85283X",
                "type": "MOON",
                "x": -20,
                "y": -14
            },
            {
                "symbol": "X1-GX37-27134F",
                "type": "MOON",
                "x": -20,
                "y": -14
            },
            {
                "symbol": "X1-GX37-24885Z",
                "type": "ASTEROID_FIELD",
                "x": -35,
                "y": 24
            },
            {
                "symbol": "X1-GX37-12756E",
                "type": "GAS_GIANT",
                "x": 23,
                "y": -49
            },
            {
                "symbol": "X1-GX37-48697D",
                "type": "ORBITAL_STATION",
                "x": 23,
                "y": -49
            },
            {
                "symbol": "X1-GX37-59618A",
                "type": "PLANET",
                "x": -72,
                "y": 9
            },
            {
                "symbol": "X1-GX37-32429A",
                "type": "JUMP_GATE",
                "x": -76,
                "y": 10
            }
        ],
        "factions": [

        ]
    },
    {
        "symbol": "X1-HH60",
        "sectorSymbol": "X1",
        "type": "RED_STAR",
        "x": -10241,
        "y": -10000,
        "waypoints": [
            {
                "symbol": "X1-HH60-21410B",
                "type": "PLANET",
                "x": -24,
                "y": -18
            },
            {
                "symbol": "X1-HH60-49311X",
                "type": "MOON",
                "x": -24,
                "y": -18
            },
            {
                "symbol": "X1-HH60-17012X",
                "type": "GAS_GIANT",
                "x": -47,
                "y": -4
            },
            {
                "symbol": "X1-HH60-93213X",
                "type": "ORBITAL_STATION",
                "x": -47,
                "y": -4
            },
            {
                "symbol": "X1-HH60-38514E",
                "type": "ASTEROID_FIELD",
                "x": -61,
                "y": -2
            },
            {
                "symbol": "X1-HH60-22115A",
                "type": "JUMP_GATE",
                "x": -51,
                "y": 63
            }
        ],
        "factions": [

        ]
    },
    {
        "symbol": "X1-TA36",
        "sectorSymbol": "X1",
        "type": "BLACK_HOLE",
        "x": -9875,
        "y": -10134,
        "waypoints": [

        ],
        "factions": [

        ]
    },
    {
        "symbol": "X1-QH31",
        "sectorSymbol": "X1",
        "type": "NEUTRON_STAR",
        "x": -10315,
        "y": -9888,
        "waypoints": [

        ],
        "factions": [

        ]
    },
    {
        "symbol": "X1-T80",
        "sectorSymbol": "X1",
        "type": "RED_STAR",
        "x": -9992,
        "y": -9538,
        "waypoints": [
            {
                "symbol": "X1-T80-84920C",
                "type": "PLANET",
                "x": -4,
                "y": -24
            },
            {
                "symbol": "X1-T80-32231F",
                "type": "MOON",
                "x": -4,
                "y": -24
            },
            {
                "symbol": "X1-T80-69182Z",
                "type": "PLANET",
                "x": -43,
                "y": -2
            },
            {
                "symbol": "X1-T80-69613Z",
                "type": "MOON",
                "x": -43,
                "y": -2
            },
            {
                "symbol": "X1-T80-55014B",
                "type": "MOON",
                "x": -43,
                "y": -2
            },
            {
                "symbol": "X1-T80-28875A",
                "type": "GAS_GIANT",
                "x": -55,
                "y": 30
            }
        ],
        "factions": [

        ]
    },
    {
        "symbol": "X1-CD78",
        "sectorSymbol": "X1",
        "type": "BLUE_STAR",
        "x": -9662,
        "y": -9694,
        "waypoints": [
            {
                "symbol": "X1-CD78-29890E",
                "type": "PLANET",
                "x": 39,
                "y": -21
            },
            {
                "symbol": "X1-CD78-52741C",
                "type": "MOON",
                "x": 39,
                "y": -21
            },
            {
                "symbol": "X1-CD78-87652F",
                "type": "MOON",
                "x": 39,
                "y": -21
            },
            {
                "symbol": "X1-CD78-77843A",
                "type": "MOON",
                "x": 39,
                "y": -21
            },
            {
                "symbol": "X1-CD78-89064A",
                "type": "PLANET",
                "x": -45,
                "y": -12
            },
            {
                "symbol": "X1-CD78-65155Z",
                "type": "MOON",
                "x": -45,
                "y": -12
            },
            {
                "symbol": "X1-CD78-65636X",
                "type": "ASTEROID_FIELD",
                "x": -39,
                "y": -40
            }
        ],
        "factions": [

        ]
    },
    {
        "symbol": "X1-UK76",
        "sectorSymbol": "X1",
        "type": "YOUNG_STAR",
        "x": -9598,
        "y": -9869,
        "waypoints": [
            {
                "symbol": "X1-UK76-80810F",
                "type": "PLANET",
                "x": -21,
                "y": -32
            },
            {
                "symbol": "X1-UK76-37231A",
                "type": "MOON",
                "x": -21,
                "y": -32
            },
            {
                "symbol": "X1-UK76-19772B",
                "type": "PLANET",
                "x": -45,
                "y": -25
            },
            {
                "symbol": "X1-UK76-96663D",
                "type": "MOON",
                "x": -45,
                "y": -25
            },
            {
                "symbol": "X1-UK76-37384B",
                "type": "MOON",
                "x": -45,
                "y": -25
            },
            {
                "symbol": "X1-UK76-81275B",
                "type": "ASTEROID_FIELD",
                "x": 10,
                "y": -56
            }
        ],
        "factions": [

        ]
    },
    {
        "symbol": "X1-MV49",
        "sectorSymbol": "X1",
        "type": "RED_STAR",
        "x": -9500,
        "y": -9915,
        "waypoints": [
            {
                "symbol": "X1-MV49-98570X",
                "type": "PLANET",
                "x": -19,
                "y": -17
            },
            {
                "symbol": "X1-MV49-60951Z",
                "type": "PLANET",
                "x": 0,
                "y": 38
            },
            {
                "symbol": "X1-MV49-91682Z",
                "type": "MOON",
                "x": 0,
                "y": 38
            },
            {
                "symbol": "X1-MV49-59803E",
                "type": "PLANET",
                "x": 36,
                "y": 37
            },
            {
                "symbol": "X1-MV49-12154D",
                "type": "MOON",
                "x": 36,
                "y": 37
            },
            {
                "symbol": "X1-MV49-87075X",
                "type": "ASTEROID_FIELD",
                "x": -10,
                "y": 73
            },
            {
                "symbol": "X1-MV49-75816A",
                "type": "ORBITAL_STATION",
                "x": -10,
                "y": 73
            },
            {
                "symbol": "X1-MV49-98117Z",
                "type": "JUMP_GATE",
                "x": 79,
                "y": 7
            }
        ],
        "factions": [

        ]
    },
    {
        "symbol": "X1-ZN66",
        "sectorSymbol": "X1",
        "type": "ORANGE_STAR",
        "x": -10443,
        "y": -10089,
        "waypoints": [
            {
                "symbol": "X1-ZN66-84170E",
                "type": "PLANET",
                "x": -26,
                "y": 7
            },
            {
                "symbol": "X1-ZN66-53761A",
                "type": "MOON",
                "x": -26,
                "y": 7
            },
            {
                "symbol": "X1-ZN66-29102B",
                "type": "MOON",
                "x": -26,
                "y": 7
            },
            {
                "symbol": "X1-ZN66-73283E",
                "type": "PLANET",
                "x": -19,
                "y": -39
            },
            {
                "symbol": "X1-ZN66-86534Z",
                "type": "MOON",
                "x": -19,
                "y": -39
            },
            {
                "symbol": "X1-ZN66-34925X",
                "type": "MOON",
                "x": -19,
                "y": -39
            },
            {
                "symbol": "X1-ZN66-72046Z",
                "type": "JUMP_GATE",
                "x": 54,
                "y": -5
            }
        ],
        "factions": [

        ]
    },
    {
        "symbol": "X1-XP96",
        "sectorSymbol": "X1",
        "type": "BLUE_STAR",
        "x": -9724,
        "y": -9417,
        "waypoints": [
            {
                "symbol": "X1-XP96-06310E",
                "type": "PLANET",
                "x": 28,
                "y": 25
            },
            {
                "symbol": "X1-XP96-11261F",
                "type": "MOON",
                "x": 28,
                "y": 25
            },
            {
                "symbol": "X1-XP96-00972B",
                "type": "MOON",
                "x": 28,
                "y": 25
            },
            {
                "symbol": "X1-XP96-36043C",
                "type": "PLANET",
                "x": 46,
                "y": 32
            },
            {
                "symbol": "X1-XP96-42444X",
                "type": "MOON",
                "x": 46,
                "y": 32
            },
            {
                "symbol": "X1-XP96-67015B",
                "type": "MOON",
                "x": 46,
                "y": 32
            },
            {
                "symbol": "X1-XP96-81946C",
                "type": "GAS_GIANT",
                "x": 47,
                "y": -53
            },
            {
                "symbol": "X1-XP96-23567B",
                "type": "ASTEROID_FIELD",
                "x": -77,
                "y": 10
            }
        ],
        "factions": [

        ]
    }
]

list_waypoint_data = [
    {
        "systemSymbol": "X1-GX37",
        "symbol": "X1-GX37-79391X",
        "type": "PLANET",
        "x": -12,
        "y": -6,
        "orbitals": [

        ],
        "traits": [
            {
                "symbol": "TOXIC_ATMOSPHERE",
                "name": "Toxic Atmosphere",
                "description": "A waypoint with a poisonous atmosphere, necessitating the use of specialized equipment and technology to protect inhabitants and visitors from harmful substances."
            },
            {
                "symbol": "VOLCANIC",
                "name": "Volcanic",
                "description": "A volatile world marked by intense volcanic activity, creating a hazardous environment with the potential for valuable resource extraction, such as rare metals and geothermal energy."
            },
            {
                "symbol": "WEAK_GRAVITY",
                "name": "Weak Gravity",
                "description": "A waypoint with a low gravitational pull, providing unique opportunities for research and industry while also challenging the adaptation of life forms and technology."
            }
        ],
        "chart": {
            "submittedBy": "COSMIC",
            "submittedOn": "2023-09-09T15:38:23.010Z"
        },
        "faction": {
            "symbol": "COSMIC"
        }
    },
    {
        "systemSymbol": "X1-GX37",
        "symbol": "X1-GX37-27130X",
        "type": "PLANET",
        "x": -20,
        "y": -14,
        "orbitals": [
            {
                "symbol": "X1-GX37-12642E"
            },
            {
                "symbol": "X1-GX37-85283X"
            },
            {
                "symbol": "X1-GX37-27134F"
            }
        ],
        "traits": [
            {
                "symbol": "OVERCROWDED",
                "name": "Overcrowded",
                "description": "A waypoint teeming with inhabitants, leading to cramped living conditions and a high demand for resources."
            },
            {
                "symbol": "HIGH_TECH",
                "name": "High-Tech",
                "description": "A center of innovation and cutting-edge technology, driving progress and attracting skilled individuals from around the galaxy."
            },
            {
                "symbol": "BUREAUCRATIC",
                "name": "Bureaucratic",
                "description": "A waypoint governed by complex regulations, red tape, and layers of administration, often leading to inefficiencies and frustration."
            },
            {
                "symbol": "TEMPERATE",
                "name": "Temperate",
                "description": "A world with a mild climate and balanced ecosystem, providing a comfortable environment for a variety of life forms and supporting diverse industries."
            },
            {
                "symbol": "MARKETPLACE",
                "name": "Marketplace",
                "description": "A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods."
            }
        ],
        "chart": {
            "submittedBy": "COSMIC",
            "submittedOn": "2023-09-09T15:38:23.038Z"
        },
        "faction": {
            "symbol": "COSMIC"
        }
    },
    {
        "systemSymbol": "X1-GX37",
        "symbol": "X1-GX37-12642E",
        "type": "MOON",
        "x": -20,
        "y": -14,
        "orbitals": [

        ],
        "traits": [
            {
                "symbol": "BARREN",
                "name": "Barren",
                "description": "A desolate world with little to no vegetation or water, presenting unique challenges for habitation and resource extraction."
            },
            {
                "symbol": "MARKETPLACE",
                "name": "Marketplace",
                "description": "A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods."
            }
        ],
        "chart": {
            "submittedBy": "COSMIC",
            "submittedOn": "2023-09-09T15:38:23.090Z"
        },
        "faction": {
            "symbol": "COSMIC"
        }
    },
    {
        "systemSymbol": "X1-GX37",
        "symbol": "X1-GX37-85283X",
        "type": "MOON",
        "x": -20,
        "y": -14,
        "orbitals": [

        ],
        "traits": [
            {
                "symbol": "VOLCANIC",
                "name": "Volcanic",
                "description": "A volatile world marked by intense volcanic activity, creating a hazardous environment with the potential for valuable resource extraction, such as rare metals and geothermal energy."
            },
            {
                "symbol": "MARKETPLACE",
                "name": "Marketplace",
                "description": "A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods."
            }
        ],
        "chart": {
            "submittedBy": "COSMIC",
            "submittedOn": "2023-09-09T15:38:23.114Z"
        },
        "faction": {
            "symbol": "COSMIC"
        }
    },
    {
        "systemSymbol": "X1-GX37",
        "symbol": "X1-GX37-27134F",
        "type": "MOON",
        "x": -20,
        "y": -14,
        "orbitals": [

        ],
        "traits": [
            {
                "symbol": "FROZEN",
                "name": "Frozen",
                "description": "An ice-covered world with frigid temperatures, providing unique research opportunities and resources such as ice water, ammonia ice, and other frozen compounds."
            },
            {
                "symbol": "MARKETPLACE",
                "name": "Marketplace",
                "description": "A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods."
            }
        ],
        "chart": {
            "submittedBy": "COSMIC",
            "submittedOn": "2023-09-09T15:38:23.134Z"
        },
        "faction": {
            "symbol": "COSMIC"
        }
    },
    {
        "systemSymbol": "X1-GX37",
        "symbol": "X1-GX37-24885Z",
        "type": "ASTEROID_FIELD",
        "x": -35,
        "y": 24,
        "orbitals": [

        ],
        "traits": [
            {
                "symbol": "MINERAL_DEPOSITS",
                "name": "Mineral Deposits",
                "description": "Abundant mineral resources, attracting mining operations and providing valuable materials such as silicon crystals and quartz sand for various industries."
            },
            {
                "symbol": "COMMON_METAL_DEPOSITS",
                "name": "Common Metal Deposits",
                "description": "A waypoint rich in common metal ores like iron, copper, and aluminum, essential for construction and manufacturing."
            },
            {
                "symbol": "STRIPPED",
                "name": "Stripped",
                "description": "A waypoint that has been heavily exploited for its resources, leaving a scarred and depleted landscape with diminished opportunities for future development."
            },
            {
                "symbol": "MARKETPLACE",
                "name": "Marketplace",
                "description": "A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods."
            }
        ],
        "chart": {
            "submittedBy": "COSMIC",
            "submittedOn": "2023-09-09T15:38:23.158Z"
        },
        "faction": {
            "symbol": "COSMIC"
        }
    },
    {
        "systemSymbol": "X1-GX37",
        "symbol": "X1-GX37-12756E",
        "type": "GAS_GIANT",
        "x": 23,
        "y": -49,
        "orbitals": [
            {
                "symbol": "X1-GX37-48697D"
            }
        ],
        "traits": [
            {
                "symbol": "VIBRANT_AURORAS",
                "name": "Vibrant Auroras",
                "description": "A celestial light show caused by the interaction of charged particles with the waypoint's atmosphere, creating a mesmerizing spectacle and attracting tourists from across the galaxy."
            },
            {
                "symbol": "STRONG_MAGNETOSPHERE",
                "name": "Strong Magnetosphere",
                "description": "A waypoint enveloped in a powerful magnetic field, potentially affecting spacecraft systems, and creating unique phenomena such as the concentration of exotic matter and graviton emitters."
            }
        ],
        "chart": {
            "submittedBy": "COSMIC",
            "submittedOn": "2023-09-09T15:38:23.179Z"
        },
        "faction": {
            "symbol": "COSMIC"
        }
    },
    {
        "systemSymbol": "X1-GX37",
        "symbol": "X1-GX37-48697D",
        "type": "ORBITAL_STATION",
        "x": 23,
        "y": -49,
        "orbitals": [

        ],
        "traits": [
            {
                "symbol": "MILITARY_BASE",
                "name": "Military Base",
                "description": "A fortified stronghold housing armed forces, advanced weaponry, and strategic assets for defense or offense."
            },
            {
                "symbol": "MARKETPLACE",
                "name": "Marketplace",
                "description": "A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods."
            },
            {
                "symbol": "SHIPYARD",
                "name": "Shipyard",
                "description": "A bustling hub for the construction, repair, and sale of various spacecraft, from humble shuttles to mighty warships."
            }
        ],
        "chart": {
            "submittedBy": "COSMIC",
            "submittedOn": "2023-09-09T15:38:23.195Z"
        },
        "faction": {
            "symbol": "COSMIC"
        }
    },
    {
        "systemSymbol": "X1-GX37",
        "symbol": "X1-GX37-59618A",
        "type": "PLANET",
        "x": -72,
        "y": 9,
        "orbitals": [

        ],
        "traits": [
            {
                "symbol": "DRY_SEABEDS",
                "name": "Dry Seabeds",
                "description": "Vast, desolate landscapes that once held oceans, now exposing the remnants of ancient marine life and providing opportunities for the discovery of valuable resources."
            },
            {
                "symbol": "WEAK_GRAVITY",
                "name": "Weak Gravity",
                "description": "A waypoint with a low gravitational pull, providing unique opportunities for research and industry while also challenging the adaptation of life forms and technology."
            },
            {
                "symbol": "MARKETPLACE",
                "name": "Marketplace",
                "description": "A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods."
            }
        ],
        "chart": {
            "submittedBy": "COSMIC",
            "submittedOn": "2023-09-09T15:38:23.236Z"
        },
        "faction": {
            "symbol": "COSMIC"
        }
    },
    {
        "systemSymbol": "X1-GX37",
        "symbol": "X1-GX37-32429A",
        "type": "JUMP_GATE",
        "x": -76,
        "y": 10,
        "orbitals": [

        ],
        "traits": [

        ],
        "chart": {
            "submittedBy": "COSMIC",
            "submittedOn": "2023-09-09T15:38:23.255Z"
        },
        "faction": {
            "symbol": "COSMIC"
        }
    }
]

market_data = {
    "symbol": "X1-GX37-59618A",
    "imports": [

    ],
    "exports": [

    ],
    "exchange": [
        {
            "symbol": "ICE_WATER",
            "name": "Fresh Water",
            "description": "High-quality fresh water, essential for life support and hydroponic agriculture."
        },
        {
            "symbol": "FOOD",
            "name": "Galactic Cuisine",
            "description": "A diverse range of foods from different planets, including fresh produce, meats, and prepared meals."
        },
        {
            "symbol": "MACHINERY",
            "name": "Machinery",
            "description": "A variety of mechanical devices and equipment, used for industrial, construction, and other practical purposes."
        },
        {
            "symbol": "ELECTRONICS",
            "name": "Electronic Components",
            "description": "Advanced electronic components used in the construction of advanced technologies."
        },
        {
            "symbol": "PLASTICS",
            "name": "Plastics",
            "description": "A wide range of plastic materials used in various applications, including packaging, construction, and manufacturing."
        },
        {
            "symbol": "FUEL",
            "name": "Fuel",
            "description": "High-energy fuel used in spacecraft propulsion systems to enable long-distance space travel."
        },
        {
            "symbol": "MEDICINE",
            "name": "Medicine",
            "description": "Medical products, including drugs, treatments, and medical equipment."
        },
        {
            "symbol": "DRUGS",
            "name": "Pharmaceuticals",
            "description": "A wide range of drugs and other medical treatments used to treat various conditions and illnesses."
        },
        {
            "symbol": "CLOTHING",
            "name": "Clothing",
            "description": "A wide range of clothing and fashion items, including garments, accessories, and textiles."
        },
        {
            "symbol": "EQUIPMENT",
            "name": "Equipment",
            "description": "Tools and equipment used in various industries and applications."
        },
        {
            "symbol": "FABRICS",
            "name": "Synthetic Fabrics",
            "description": "High-tech fabrics used in the production of clothing and other products for everyday use."
        }
    ]
}

shipyard_data = {
    "symbol": "X1-GX37-48697D",
    "shipTypes": [
        {
            "type": "SHIP_PROBE"
        },
        {
            "type": "SHIP_ORE_HOUND"
        },
        {
            "type": "SHIP_LIGHT_HAULER"
        },
        {
            "type": "SHIP_REFINING_FREIGHTER"
        },
        {
            "type": "SHIP_MINING_DRONE"
        }
    ],
    "transactions": [
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "SY94J60OWZF63O",
            "price": 93865,
            "timestamp": "2023-09-10T17:57:37.169Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "9BHJHB6V_Q25DA",
            "price": 93861,
            "timestamp": "2023-09-10T17:57:03.122Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "CV1VDVEVUHVXFJ",
            "price": 93857,
            "timestamp": "2023-09-10T17:56:26.574Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "BRH0WPB7_RIL7G",
            "price": 93853,
            "timestamp": "2023-09-10T17:55:51.676Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "YWYMS00F7H64S3",
            "price": 93849,
            "timestamp": "2023-09-10T17:55:20.835Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "3KXFEVZ9EQXMTA",
            "price": 93845,
            "timestamp": "2023-09-10T17:54:34.962Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "ZN_9BK6MVMET6_",
            "price": 93841,
            "timestamp": "2023-09-10T17:54:05.170Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "D8SG87W9QQV09C",
            "price": 93837,
            "timestamp": "2023-09-10T17:53:29.225Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "O0M1R9TFOWE8B5",
            "price": 93833,
            "timestamp": "2023-09-10T17:52:56.136Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "2MMO8QYVT4NMMS",
            "price": 93829,
            "timestamp": "2023-09-10T17:52:23.235Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "FAJ0YNHELAKRVV",
            "price": 93825,
            "timestamp": "2023-09-10T17:51:47.636Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "Z8UUOPBLMGPD1_",
            "price": 93821,
            "timestamp": "2023-09-10T17:51:13.694Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "P6GN2E0_734JTH",
            "price": 93817,
            "timestamp": "2023-09-10T17:50:40.793Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "CTRI-U-",
            "price": 93813,
            "timestamp": "2023-09-10T17:50:22.833Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "QZCI05M8_XZ5SM",
            "price": 93809,
            "timestamp": "2023-09-10T17:50:04.598Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "UV9W3N7Y038QO6",
            "price": 93805,
            "timestamp": "2023-09-10T17:49:30.401Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "GWONJ82YJ_A5KB",
            "price": 93801,
            "timestamp": "2023-09-10T17:48:54.534Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "Y1M979VRQ4_PYT",
            "price": 93798,
            "timestamp": "2023-09-10T17:48:15.782Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "OZ6I__O9SSUH5U",
            "price": 93794,
            "timestamp": "2023-09-10T17:47:44.287Z"
        },
        {
            "shipSymbol": "SHIP_MINING_DRONE",
            "waypointSymbol": "X1-GX37-48697D",
            "agentSymbol": "GAPNK7HV_0RCMG",
            "price": 93790,
            "timestamp": "2023-09-10T17:47:08.536Z"
        }
    ],
    "ships": [
        {
            "type": "SHIP_PROBE",
            "name": "Probe Satellite",
            "description": "A small, unmanned spacecraft that can be launched into orbit to gather data and perform basic tasks.",
            "purchasePrice": 68991,
            "frame": {
                "symbol": "FRAME_PROBE",
                "name": "Frame Probe",
                "description": "A small, unmanned spacecraft used for exploration, reconnaissance, and scientific research.",
                "moduleSlots": 0,
                "mountingPoints": 0,
                "fuelCapacity": 0,
                "requirements": {
                    "power": 1,
                    "crew": 0
                }
            },
            "reactor": {
                "symbol": "REACTOR_SOLAR_I",
                "name": "Solar Reactor I",
                "description": "A basic solar power reactor, used to generate electricity from solar energy.",
                "powerOutput": 3,
                "requirements": {
                    "crew": 0
                }
            },
            "engine": {
                "symbol": "ENGINE_IMPULSE_DRIVE_I",
                "name": "Impulse Drive I",
                "description": "A basic low-energy propulsion system that generates thrust for interplanetary travel.",
                "speed": 2,
                "requirements": {
                    "power": 1,
                    "crew": 0
                }
            },
            "modules": [

            ],
            "mounts": [

            ]
        },
        {
            "type": "SHIP_ORE_HOUND",
            "name": "Ore Hound",
            "description": "The Ore Hound is a specialized mining ship designed for extracting valuable ores and minerals from asteroids and other celestial bodies. With its advanced mining lasers and reinforced hull, the Ore Hound is capable of excavating large amounts of ore and minerals from even the toughest asteroids. It is equipped with a range of modules and mounts for handling a variety of mining and defensive needs, and is an essential vessel for miners and traders looking to profit from the rich resources of the galaxy.",
            "purchasePrice": 266226,
            "frame": {
                "symbol": "FRAME_MINER",
                "name": "Frame Miner",
                "description": "A medium-sized spacecraft designed for mining operations and resource extraction.",
                "moduleSlots": 5,
                "mountingPoints": 3,
                "fuelCapacity": 900,
                "requirements": {
                    "power": 5,
                    "crew": 15
                }
            },
            "reactor": {
                "symbol": "REACTOR_FISSION_I",
                "name": "Fission Reactor I",
                "description": "A basic fission power reactor, used to generate electricity from nuclear fission reactions.",
                "powerOutput": 31,
                "requirements": {
                    "crew": 8
                }
            },
            "engine": {
                "symbol": "ENGINE_ION_DRIVE_I",
                "name": "Ion Drive I",
                "description": "An advanced propulsion system that uses ionized particles to generate high-speed, low-thrust acceleration.",
                "speed": 10,
                "requirements": {
                    "power": 3,
                    "crew": 3
                }
            },
            "modules": [
                {
                    "symbol": "MODULE_CARGO_HOLD_I",
                    "name": "Cargo Hold",
                    "description": "A module that increases a ship's cargo capacity.",
                    "capacity": 30,
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CARGO_HOLD_I",
                    "name": "Cargo Hold",
                    "description": "A module that increases a ship's cargo capacity.",
                    "capacity": 30,
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_MINERAL_PROCESSOR_I",
                    "name": "Mineral Processor",
                    "description": "Crushes and processes extracted minerals and ores into their component parts, filters out impurities, and containerizes them into raw storage units.",
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 2
                    }
                },
                {
                    "symbol": "MODULE_CREW_QUARTERS_I",
                    "name": "Crew Quarters",
                    "description": "A module that provides living space and amenities for the crew.",
                    "capacity": 40,
                    "requirements": {
                        "crew": 2,
                        "power": 1,
                        "slots": 1
                    }
                }
            ],
            "mounts": [
                {
                    "symbol": "MOUNT_MINING_LASER_II",
                    "name": "Mining Laser II",
                    "description": "An advanced mining laser that is more efficient and effective at extracting valuable minerals from asteroids and other space objects.",
                    "strength": 25,
                    "requirements": {
                        "crew": 2,
                        "power": 2
                    }
                },
                {
                    "symbol": "MOUNT_SURVEYOR_I",
                    "name": "Surveyor I",
                    "description": "A basic survey probe that can be used to gather information about a mineral deposit.",
                    "strength": 1,
                    "deposits": [
                        "QUARTZ_SAND",
                        "SILICON_CRYSTALS",
                        "PRECIOUS_STONES",
                        "ICE_WATER",
                        "AMMONIA_ICE",
                        "IRON_ORE",
                        "COPPER_ORE",
                        "SILVER_ORE",
                        "ALUMINUM_ORE",
                        "GOLD_ORE",
                        "PLATINUM_ORE"
                    ],
                    "requirements": {
                        "crew": 2,
                        "power": 1
                    }
                }
            ]
        },
        {
            "type": "SHIP_LIGHT_HAULER",
            "name": "Light Hauler",
            "description": "A small, fast cargo ship that is designed for short-range transport of light loads.",
            "purchasePrice": 333678,
            "frame": {
                "symbol": "FRAME_LIGHT_FREIGHTER",
                "name": "Frame Light Freighter",
                "description": "A small, versatile spacecraft used for cargo transport and other commercial operations.",
                "moduleSlots": 6,
                "mountingPoints": 1,
                "fuelCapacity": 1700,
                "requirements": {
                    "power": 5,
                    "crew": 40
                }
            },
            "reactor": {
                "symbol": "REACTOR_CHEMICAL_I",
                "name": "Chemical Reactor I",
                "description": "A basic chemical power reactor, used to generate electricity from chemical reactions.",
                "powerOutput": 15,
                "requirements": {
                    "crew": 3
                }
            },
            "engine": {
                "symbol": "ENGINE_ION_DRIVE_I",
                "name": "Ion Drive I",
                "description": "An advanced propulsion system that uses ionized particles to generate high-speed, low-thrust acceleration.",
                "speed": 10,
                "requirements": {
                    "power": 3,
                    "crew": 3
                }
            },
            "modules": [
                {
                    "symbol": "MODULE_CARGO_HOLD_I",
                    "name": "Cargo Hold",
                    "description": "A module that increases a ship's cargo capacity.",
                    "capacity": 30,
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CARGO_HOLD_I",
                    "name": "Cargo Hold",
                    "description": "A module that increases a ship's cargo capacity.",
                    "capacity": 30,
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CARGO_HOLD_I",
                    "name": "Cargo Hold",
                    "description": "A module that increases a ship's cargo capacity.",
                    "capacity": 30,
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CARGO_HOLD_I",
                    "name": "Cargo Hold",
                    "description": "A module that increases a ship's cargo capacity.",
                    "capacity": 30,
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CREW_QUARTERS_I",
                    "name": "Crew Quarters",
                    "description": "A module that provides living space and amenities for the crew.",
                    "capacity": 40,
                    "requirements": {
                        "crew": 2,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CREW_QUARTERS_I",
                    "name": "Crew Quarters",
                    "description": "A module that provides living space and amenities for the crew.",
                    "capacity": 40,
                    "requirements": {
                        "crew": 2,
                        "power": 1,
                        "slots": 1
                    }
                }
            ],
            "mounts": [
                {
                    "symbol": "MOUNT_SURVEYOR_I",
                    "name": "Surveyor I",
                    "description": "A basic survey probe that can be used to gather information about a mineral deposit.",
                    "strength": 1,
                    "deposits": [
                        "QUARTZ_SAND",
                        "SILICON_CRYSTALS",
                        "PRECIOUS_STONES",
                        "ICE_WATER",
                        "AMMONIA_ICE",
                        "IRON_ORE",
                        "COPPER_ORE",
                        "SILVER_ORE",
                        "ALUMINUM_ORE",
                        "GOLD_ORE",
                        "PLATINUM_ORE"
                    ],
                    "requirements": {
                        "crew": 2,
                        "power": 1
                    }
                }
            ]
        },
        {
            "type": "SHIP_REFINING_FREIGHTER",
            "name": "Refining Freighter",
            "description": "A large cargo ship designed specifically for refining raw materials. Equipped with a powerful reactor and space for large modules, the refining freighter is a versatile and convenient tool for industrial operations in remote or difficult-to-reach locations.",
            "purchasePrice": 1730288,
            "frame": {
                "symbol": "FRAME_HEAVY_FREIGHTER",
                "name": "Frame Heavy Freighter",
                "description": "A large, heavily-armed spacecraft used for cargo transport and other commercial operations in hostile environments.",
                "moduleSlots": 12,
                "mountingPoints": 3,
                "fuelCapacity": 2300,
                "requirements": {
                    "power": 10,
                    "crew": 100
                }
            },
            "reactor": {
                "symbol": "REACTOR_FUSION_I",
                "name": "Fusion Reactor I",
                "description": "A basic fusion power reactor, used to generate electricity from nuclear fusion reactions.",
                "powerOutput": 40,
                "requirements": {
                    "crew": 12
                }
            },
            "engine": {
                "symbol": "ENGINE_ION_DRIVE_II",
                "name": "Ion Drive II",
                "description": "An advanced propulsion system that uses ionized particles to generate high-speed, low-thrust acceleration, with improved efficiency and performance.",
                "speed": 30,
                "requirements": {
                    "power": 6,
                    "crew": 8
                }
            },
            "modules": [
                {
                    "symbol": "MODULE_CARGO_HOLD_I",
                    "name": "Cargo Hold",
                    "description": "A module that increases a ship's cargo capacity.",
                    "capacity": 30,
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CARGO_HOLD_I",
                    "name": "Cargo Hold",
                    "description": "A module that increases a ship's cargo capacity.",
                    "capacity": 30,
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CARGO_HOLD_I",
                    "name": "Cargo Hold",
                    "description": "A module that increases a ship's cargo capacity.",
                    "capacity": 30,
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CARGO_HOLD_I",
                    "name": "Cargo Hold",
                    "description": "A module that increases a ship's cargo capacity.",
                    "capacity": 30,
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CREW_QUARTERS_I",
                    "name": "Crew Quarters",
                    "description": "A module that provides living space and amenities for the crew.",
                    "capacity": 40,
                    "requirements": {
                        "crew": 2,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CREW_QUARTERS_I",
                    "name": "Crew Quarters",
                    "description": "A module that provides living space and amenities for the crew.",
                    "capacity": 40,
                    "requirements": {
                        "crew": 2,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CREW_QUARTERS_I",
                    "name": "Crew Quarters",
                    "description": "A module that provides living space and amenities for the crew.",
                    "capacity": 40,
                    "requirements": {
                        "crew": 2,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_CREW_QUARTERS_I",
                    "name": "Crew Quarters",
                    "description": "A module that provides living space and amenities for the crew.",
                    "capacity": 40,
                    "requirements": {
                        "crew": 2,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_ORE_REFINERY_I",
                    "name": "Ore Refinery",
                    "description": "A specialized module that can refine raw ores into usable metals and other materials.",
                    "production": [
                        "IRON",
                        "COPPER",
                        "SILVER",
                        "GOLD",
                        "ALUMINUM",
                        "PLATINUM",
                        "URANITE",
                        "MERITIUM"
                    ],
                    "requirements": {
                        "crew": 20,
                        "power": 12,
                        "slots": 4
                    }
                }
            ],
            "mounts": [
                {
                    "symbol": "MOUNT_TURRET_I",
                    "name": "Rotary Cannon",
                    "description": "A rotary cannon is a type of mounted turret that is designed to fire a high volume of rounds in rapid succession.",
                    "requirements": {
                        "power": 1,
                        "crew": 1
                    }
                },
                {
                    "symbol": "MOUNT_TURRET_I",
                    "name": "Rotary Cannon",
                    "description": "A rotary cannon is a type of mounted turret that is designed to fire a high volume of rounds in rapid succession.",
                    "requirements": {
                        "power": 1,
                        "crew": 1
                    }
                },
                {
                    "symbol": "MOUNT_MISSILE_LAUNCHER_I",
                    "name": "Missile Launcher",
                    "description": "A basic missile launcher that fires guided missiles with a variety of warheads for different targets.",
                    "requirements": {
                        "power": 1,
                        "crew": 2
                    }
                }
            ]
        },
        {
            "type": "SHIP_MINING_DRONE",
            "name": "Mining Drone",
            "description": "A small, unmanned spacecraft that can be used for mining operations, such as extracting valuable minerals from asteroids.",
            "purchasePrice": 93869,
            "frame": {
                "symbol": "FRAME_DRONE",
                "name": "Frame Drone",
                "description": "A small, unmanned spacecraft used for various tasks, such as surveillance, transportation, or combat.",
                "moduleSlots": 3,
                "mountingPoints": 2,
                "fuelCapacity": 100,
                "requirements": {
                    "power": 1,
                    "crew": -3
                }
            },
            "reactor": {
                "symbol": "REACTOR_CHEMICAL_I",
                "name": "Chemical Reactor I",
                "description": "A basic chemical power reactor, used to generate electricity from chemical reactions.",
                "powerOutput": 15,
                "requirements": {
                    "crew": 3
                }
            },
            "engine": {
                "symbol": "ENGINE_IMPULSE_DRIVE_I",
                "name": "Impulse Drive I",
                "description": "A basic low-energy propulsion system that generates thrust for interplanetary travel.",
                "speed": 2,
                "requirements": {
                    "power": 1,
                    "crew": 0
                }
            },
            "modules": [
                {
                    "symbol": "MODULE_CARGO_HOLD_I",
                    "name": "Cargo Hold",
                    "description": "A module that increases a ship's cargo capacity.",
                    "capacity": 30,
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 1
                    }
                },
                {
                    "symbol": "MODULE_MINERAL_PROCESSOR_I",
                    "name": "Mineral Processor",
                    "description": "Crushes and processes extracted minerals and ores into their component parts, filters out impurities, and containerizes them into raw storage units.",
                    "requirements": {
                        "crew": 0,
                        "power": 1,
                        "slots": 2
                    }
                }
            ],
            "mounts": [
                {
                    "symbol": "MOUNT_MINING_LASER_I",
                    "name": "Mining Laser I",
                    "description": "A basic mining laser that can be used to extract valuable minerals from asteroids and other space objects.",
                    "strength": 10,
                    "requirements": {
                        "crew": 0,
                        "power": 1
                    }
                }
            ]
        }
    ]
}

jumpgate_data = {
    "jumpRange": 2000,
    "factionSymbol": "COSMIC",
    "connectedSystems": [
        {
            "symbol": "X1-MV49",
            "sectorSymbol": "X1",
            "type": "RED_STAR",
            "factionSymbol": "COSMIC",
            "x": -9500,
            "y": -9915,
            "distance": 446
        },
        {
            "symbol": "X1-HH60",
            "sectorSymbol": "X1",
            "type": "RED_STAR",
            "factionSymbol": "COSMIC",
            "x": -10241,
            "y": -10000,
            "distance": 451
        },
        {
            "symbol": "X1-ZN66",
            "sectorSymbol": "X1",
            "type": "ORANGE_STAR",
            "factionSymbol": "COSMIC",
            "x": -10443,
            "y": -10089,
            "distance": 666
        },
        {
            "symbol": "X1-TJ8",
            "sectorSymbol": "X1",
            "type": "ORANGE_STAR",
            "factionSymbol": "COSMIC",
            "x": -8909,
            "y": -9622,
            "distance": 991
        },
        {
            "symbol": "X1-MS67",
            "sectorSymbol": "X1",
            "type": "RED_STAR",
            "factionSymbol": "COSMIC",
            "x": -9082,
            "y": -8594,
            "distance": 1381
        },
        {
            "symbol": "X1-FQ51",
            "sectorSymbol": "X1",
            "type": "BLUE_STAR",
            "factionSymbol": "COSMIC",
            "x": -8639,
            "y": -10604,
            "distance": 1543
        },
        {
            "symbol": "X1-TR54",
            "sectorSymbol": "X1",
            "type": "RED_STAR",
            "factionSymbol": "COSMIC",
            "x": -8282,
            "y": -9669,
            "distance": 1614
        },
        {
            "symbol": "X1-QB80",
            "sectorSymbol": "X1",
            "type": "BLUE_STAR",
            "factionSymbol": "COSMIC",
            "x": -9562,
            "y": -11304,
            "distance": 1630
        },
        {
            "symbol": "X1-BQ83",
            "sectorSymbol": "X1",
            "type": "YOUNG_STAR",
            "factionSymbol": "COSMIC",
            "x": -11235,
            "y": -8665,
            "distance": 1698
        },
        {
            "symbol": "X1-JD39",
            "sectorSymbol": "X1",
            "type": "ORANGE_STAR",
            "factionSymbol": "COSMIC",
            "x": -8746,
            "y": -11017,
            "distance": 1742
        },
        {
            "symbol": "X1-NQ20",
            "sectorSymbol": "X1",
            "type": "BLUE_STAR",
            "factionSymbol": "COSMIC",
            "x": -11112,
            "y": -11164,
            "distance": 1896
        },
        {
            "symbol": "X1-GP11",
            "sectorSymbol": "X1",
            "type": "ORANGE_STAR",
            "factionSymbol": "COSMIC",
            "x": -10518,
            "y": -7902,
            "distance": 1911
        },
        {
            "symbol": "X1-AV42",
            "sectorSymbol": "X1",
            "type": "RED_STAR",
            "factionSymbol": "COSMIC",
            "x": -11661,
            "y": -10568,
            "distance": 1963
        }
    ]
}
