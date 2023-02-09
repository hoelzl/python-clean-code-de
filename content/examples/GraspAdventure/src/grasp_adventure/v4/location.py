from dataclasses import dataclass, field
from typing import Any, Sequence, Mapping, Dict, List
import sys

from .base_classes import Action


LocationDescription = Mapping[str, Any]
LocationDescriptions = Sequence[LocationDescription]


@dataclass
class Location:
    name: str
    connections: Dict[str, "Location"] = field(default_factory=dict)

    def __getitem__(self, direction: str) -> "Location":
        return self.connections.get(direction)

    @property
    def move_actions(self) -> List[Action]:
        from .actions import MoveAction

        return [
            MoveAction(direction, location)
            for direction, location in self.connections.items()
        ]
