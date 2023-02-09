from grasp_adventure.v3b.world_factory import WorldFactory
from grasp_adventure.data.locations import simple_locations


def test_connections():
    level = WorldFactory().create(simple_locations)
    assert level["Room 1"].connections["north"] == level["Room 2"]
    assert level["Room 2"].connections["south"] == level["Room 1"]
    assert level["Room 1"].connections.get("east") is None


def test_getitem():
    level = WorldFactory().create(simple_locations)
    assert level["Room 1"]["north"] == level["Room 2"]
    assert level["Room 2"]["south"] == level["Room 1"]
    assert level["Room 1"]["east"] is None
