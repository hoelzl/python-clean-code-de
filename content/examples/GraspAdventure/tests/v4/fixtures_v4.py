from grasp_adventure.data.locations import simple_locations
from grasp_adventure.v4.game_factory import GameFactory
from grasp_adventure.v4.pawn import Pawn
from grasp_adventure.v4.player import Player

import pytest


@pytest.fixture()
def level():
    return GameFactory().create_world(simple_locations)


@pytest.fixture()
def pawn(level):
    return Pawn(location=level["Room 1"])


@pytest.fixture()
def player(level):
    pawn = Pawn(location=level["Room 1"])
    return Player(name="The Player", pawn=pawn)
