from grasp_adventure.v5.actions import MoveAction, WaitAction
from fixtures_v5 import *  # noqa


def test_player_location(player, level):
    assert player.location == level["Room 1"]


def test_actions(player, level):
    actions = player.actions

    assert actions == [MoveAction("north", level["Room 2"]), WaitAction()]


def test_select_action(player, level):
    assert player.select_action() == MoveAction("north", level["Room 2"])


def test_perform_move_action(player, level):
    action = MoveAction(direction="north", target=level["Room 2"])
    player.perform_action(action)
    assert player.location == level["Room 2"]


def test_perform_wait_action(player, level):
    action = WaitAction()
    player.perform_action(action)
    assert player.location == level["Room 1"]


def test_take_turn(player, level):
    player.take_turn()
    assert player.location == level["Room 2"]
