from grasp_adventure.v5.actions import MoveAction
from fixtures_v5 import *  # noqa


def test_connections():
    level = GameFactory().create_world(simple_locations)
    assert level["Room 1"].connections["north"] == level["Room 2"]
    assert level["Room 2"].connections["south"] == level["Room 1"]
    assert level["Room 1"].connections.get("east") is None


def test_getitem():
    level = GameFactory().create_world(simple_locations)
    assert level["Room 1"]["north"] == level["Room 2"]
    assert level["Room 2"]["south"] == level["Room 1"]
    assert level["Room 1"]["east"] is None


def test_move_actions():
    level = GameFactory().create_world(simple_locations)
    assert level["Room 1"].move_actions == [MoveAction("north", level["Room 2"])]
