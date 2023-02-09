from dataclasses import dataclass, field
from typing import Any, Sequence, Mapping, Dict
import sys


LocationDescription = Mapping[str, Any]
LocationDescriptions = Sequence[LocationDescription]


@dataclass
class Location:
    name: str
    connections: Dict[str, "Location"] = field(default_factory=dict)

    def __getitem__(self, direction: str) -> "Location":
        return self.connections.get(direction)
