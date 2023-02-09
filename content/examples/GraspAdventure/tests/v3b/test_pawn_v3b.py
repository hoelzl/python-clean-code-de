from grasp_adventure.data.locations import simple_locations
from grasp_adventure.v3b.pawn import Action, Pawn
from grasp_adventure.v3b.world_factory import WorldFactory

import pytest


@pytest.fixture()
def pawn_and_level():
    level = WorldFactory().create(simple_locations)
    pawn = Pawn(name="My Pawn", location=level["Room 1"])
    return pawn, level


def test_valid_move(pawn_and_level):
    pawn, level = pawn_and_level
    pawn.perform_action(Action.MOVE, "north")
    assert pawn.location == level["Room 2"]


def test_invalid_move(pawn_and_level, capsys):
    pawn, level = pawn_and_level
    pawn.perform_action(Action.MOVE, "east")

    assert pawn.location == level["Room 1"]
    output = capsys.readouterr().out.strip()
    assert output == "'My Pawn': Cannot move in direction 'east'."


def test_invalid_action(pawn_and_level, capsys):
    pawn, level = pawn_and_level
    pawn.perform_action("Invalid Action", "???")

    assert pawn.location == level["Room 1"]
    output = capsys.readouterr().out.strip()
    assert output == "Unknown action: 'Invalid Action'"
