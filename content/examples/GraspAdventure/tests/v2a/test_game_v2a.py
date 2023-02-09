from grasp_adventure.v2a.world import World
from grasp_adventure.data.locations import simple_locations


def test_connection():
    game = World.from_location_descriptions(simple_locations)
    assert game.connection(game["Room 1"], "north") == game["Room 2"]
    assert game.connection(game["Room 2"], "south") == game["Room 1"]
    assert game.connection(game["Room 1"], "east") is None
