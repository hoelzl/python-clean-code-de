from grasp_adventure.data.locations import simple_locations
from grasp_adventure.v3c.action import MoveAction
from grasp_adventure.v3c.world_factory import WorldFactory
from grasp_adventure.v3c.pawn import Pawn

import pytest


@pytest.fixture()
def level():
    return WorldFactory().create(simple_locations)


@pytest.fixture()
def player(level):
    return Pawn(name="My Pawn", location=level["Room 1"])


def test_valid_move(player, level):
    action = MoveAction(direction="north", target=level["Room 2"])
    player.perform(action)
    assert player.location == level["Room 2"]
