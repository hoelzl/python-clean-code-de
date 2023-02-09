from grasp_adventure.v5.game_objects import TreasureChest
from fixtures_v5 import *  # noqa


def test_str_of_treasure_chest():
    tc = TreasureChest()
    assert str(tc) == "a treasure chest"


def test_description_of_treasure_chest():
    tc = TreasureChest(gold=120)
    assert tc.description == "a treasure chest containing 120 gold pieces"
