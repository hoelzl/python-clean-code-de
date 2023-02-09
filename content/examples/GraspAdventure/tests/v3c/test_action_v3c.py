from grasp_adventure.data.locations import simple_locations
from grasp_adventure.v3c.action import MoveAction
from grasp_adventure.v3c.world_factory import WorldFactory

import pytest


@pytest.fixture()
def level():
    return WorldFactory().create(simple_locations)


def test_action_description(level):
    action = MoveAction(direction="north", target=level["Room 2"])
    assert action.description == "move north to Room 2"
