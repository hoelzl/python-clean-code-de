from dataclasses import dataclass
from enum import Enum

from .location import Location


class Action(str, Enum):
    MOVE = "move"


@dataclass
class Pawn:
    name: str
    location: Location

    def perform_action(self, action: Action, direction: str):
        if action == Action.MOVE:
            new_location = self.location[direction]
            if new_location:
                self.location = new_location
            else:
                print(f"{self.name!r}: Cannot move in direction {direction!r}.")
        else:
            print(f"Unknown action: {action!r}")
