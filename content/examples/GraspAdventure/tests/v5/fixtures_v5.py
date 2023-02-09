from grasp_adventure.data.locations import simple_locations
from grasp_adventure.v5.game_objects import TreasureChest
from grasp_adventure.v5.game_factory import GameFactory
from grasp_adventure.v5.pawn import Pawn
from grasp_adventure.v5.player import Player

import pytest


@pytest.fixture()
def a_treasure_chest_description():
    return {
        "A Treasure Chest": {
            "class_name": "TreasureChest",
            "kwargs": {"gold": 100},
        }
    }


@pytest.fixture()
def object_classes():
    return {"TreasureChest": TreasureChest}


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
