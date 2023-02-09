from dataclasses import dataclass, field
from typing import Any, Dict
import sys

from .location import Location



LocationDict = Dict[str, Location]


@dataclass
class World:
    locations: LocationDict
    initial_location_name: str

    def __getitem__(self, location_name: str):
        """Return the connected location in direction `location_name`.

        >>> from grasp_adventure.v3c.world_factory import WorldFactory
        >>> level = WorldFactory().create([{"name": "A"}, {"name": "B"}])
        >>> level["A"]
        Location(name='A', connections={})
        >>> level["B"]
        Location(name='B', connections={})
        >>> level["C"]
        Traceback (most recent call last):
        ...
        KeyError: 'C'
        """
        return self.locations[location_name]
