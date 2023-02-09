from grasp_adventure.data.locations import simple_locations
from grasp_adventure.v3a.pawn import Pawn
from grasp_adventure.v3a.world_factory import LevelFactory

import pytest


@pytest.fixture()
def pawn_and_level():
    level = LevelFactory().create(simple_locations)
    pawn = Pawn(name="My Pawn", location=level["Room 1"])
    return pawn, level


def test_valid_move(pawn_and_level):
    pawn, level = pawn_and_level
    pawn.move("north")
    assert pawn.location == level["Room 2"]


def test_invalid_move(pawn_and_level, capsys):
    pawn, level = pawn_and_level
    pawn.move("east")

    assert pawn.location == level["Room 1"]
    output = capsys.readouterr().out.strip()
    assert output == "'My Pawn': Cannot move in direction 'east'."
