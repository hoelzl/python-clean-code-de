from grasp_adventure.v4.actions import MoveAction
from fixtures_v4 import *  # noqa


def test_move_action_description(level):
    action = MoveAction(direction="north", target=level["Room 2"])
    assert action.description == "move north to Room 2"
