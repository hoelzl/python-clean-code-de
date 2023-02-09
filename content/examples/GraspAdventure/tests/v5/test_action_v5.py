from grasp_adventure.v5.actions import InspectAction, MoveAction
from grasp_adventure.v5.game_objects import TreasureChest
from fixtures_v5 import *  # noqa


def test_move_action_description(level):
    action = MoveAction(direction="north", target=level["Room 2"])
    assert action.description == "move north to Room 2"


def test_inspect_action_description():
    action = InspectAction(TreasureChest())
    assert action.description == "inspect a treasure chest"
