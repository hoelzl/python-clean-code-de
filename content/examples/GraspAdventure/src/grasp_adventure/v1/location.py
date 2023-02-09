from dataclasses import dataclass
from typing import Any, Sequence, Mapping

LocationDescription = Mapping[str, Any]
LocationDescriptions = Sequence[LocationDescription]


@dataclass
class Location:
    name: str
