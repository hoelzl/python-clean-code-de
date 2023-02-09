simple_locations = [
    {"name": "Room 1",
     "connections": {"north": "Room 2"}},
    {"name": "Room 2",
     "connections": {"south": "Room 1"}}
]

dungeon_locations = [
    {"name": "Vestibule",
     "connections": {"north": "Entrance Hall"}},
    {"name": "Entrance Hall",
     "connections": {"west": "Dark Corridor", "east": "Brightly Lit Corridor", "south": "Vestibule"}},
    {"name": "Dark Corridor",
     "connections": {"west": "Treasure Chamber", "east": "Entrance Hall"}},
    {"name": "Brightly Lit Corridor",
     "connections": {"west": "Entrance Hall"},
     "objects": ["Torch"]},
    {"name": "Treasure Chamber",
     "connections": {"east": "Dark Corridor"},
     "objects": ["Treasure Chest"]},
]
