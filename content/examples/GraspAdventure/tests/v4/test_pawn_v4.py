from grasp_adventure.v4.actions import MoveAction, WaitAction
from fixtures_v4 import *  # noqa


def test_actions(pawn, level):
    actions = pawn.actions

    assert actions == [MoveAction("north", level["Room 2"])]
