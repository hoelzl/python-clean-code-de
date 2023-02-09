from dataclasses import dataclass
from typing import TYPE_CHECKING

from .location import Location

if TYPE_CHECKING:
    from .action import Action


@dataclass
class Pawn:
    name: str
    location: Location

    def perform(self, action: "Action"):
        action.execute(self)
