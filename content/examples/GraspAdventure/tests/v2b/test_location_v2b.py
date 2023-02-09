from grasp_adventure.v2b.world import World
from grasp_adventure.data.locations import simple_locations


def test_connections():
    game = World.from_location_descriptions(simple_locations)
    assert game["Room 1"].connections["north"] == game["Room 2"]
    assert game["Room 2"].connections["south"] == game["Room 1"]
    assert game["Room 1"].connections.get("east") is None


def test_getitem():
    game = World.from_location_descriptions(simple_locations)
    assert game["Room 1"]["north"] == game["Room 2"]
    assert game["Room 2"]["south"] == game["Room 1"]
    assert game["Room 1"]["east"] is None
