from dataclasses import dataclass
from random import choice
from typing import Callable, List

from .base_classes import Action
from .location import Location
from .pawn import Pawn


def first_action_strategy(actions: List[Action]):
    """Return the first available action.

    If no action is available, return a wait action."""

    if actions:
        return actions[0]
    else:
        from .actions import WaitAction

        return WaitAction()


def random_action_strategy(actions: List[Action]):
    """Return a random choice from the available actions.

    If no action is available, return a wait action."""

    if actions:
        return choice(actions)
    else:
        from .actions import WaitAction

        return WaitAction()


@dataclass
class Player:
    name: str
    pawn: Pawn
    action_selection_strategy: Callable[[List[Action]], Action] = first_action_strategy

    @property
    def location(self) -> Location:
        return self.pawn.location

    @location.setter
    def location(self, new_location: Location):
        self.pawn.location = new_location

    @property
    def description(self) -> str:
        return f"{self.name} at {self.location.name}"

    @property
    def actions(self) -> List[Action]:
        from .actions import WaitAction

        return [*self.pawn.actions, WaitAction()]

    def select_action(self) -> Action:
        return self.action_selection_strategy(self.actions)

    def perform_action(self, action: "Action"):
        action.execute(self)

    def take_turn(self):
        action = self.select_action()
        self.perform_action(action)
