from dataclasses import dataclass
from typing import List

from .base_classes import Action
from .location import Location


@dataclass
class Pawn:
    location: Location

    @property
    def actions(self) -> List[Action]:
        return self.location.move_actions
