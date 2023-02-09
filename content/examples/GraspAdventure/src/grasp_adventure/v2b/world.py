from dataclasses import dataclass
from typing import Dict

from .location import Location, LocationDescriptions

LocationDict = Dict[str, Location]


@dataclass
class World:
    locations: LocationDict
    initial_location_name: str

    def __getitem__(self, location_name: str):
        """Return the connected location in direction `location_name`.

        >>> world = World.from_location_descriptions([{"name": "A"}, {"name": "B"}])
        >>> world["A"]
        Location(name='A', connections={})
        >>> world["B"]
        Location(name='B', connections={})
        >>> world["C"]
        Traceback (most recent call last):
        ...
        KeyError: 'C'
        """
        return self.locations[location_name]

    @classmethod
    def from_location_descriptions(
        cls, location_descriptions: LocationDescriptions
    ) -> "World":
        """Create a World from a description of its locations.

        >>> World.from_location_descriptions(
        ...         [{"name": "A", "connections": {"east": "B"}},
        ...          {"name": "B", "connections": {"west": "A"}}])
        World(locations={'A': Location(name='A', connections={'east': ...}),
                            'B': Location(name='B', connections={'west': ...})},
              initial_location_name='A')
        """
        return cls(
            locations=(_create_locations(location_descriptions)),
            initial_location_name=location_descriptions[0]["name"],
        )


def _create_locations(location_descriptions: LocationDescriptions) -> LocationDict:
    """Create a location dictionary from descriptions.

    >>> _create_locations(
    ...         [{"name": "A", "connections": {"east": "B"}},
    ...          {"name": "B", "connections": {"west": "A"}}])
    {'A': Location(name='A',
          connections={'east': Location(name='B', connections={'west': ...})}),
     'B': Location(name='B',
          connections={'west': Location(name='A', connections={'east': ...})})}
    """
    locations = _create_locations_without_connections(location_descriptions)
    _build_connections_for_all_locations(locations, location_descriptions)
    return locations


def _create_locations_without_connections(
    location_descriptions: LocationDescriptions,
) -> LocationDict:
    locations = {
        location_description["name"]: Location(location_description["name"])
        for location_description in location_descriptions
    }
    return locations


def _build_connections_for_all_locations(
    locations: LocationDict, location_descriptions: LocationDescriptions
):
    for location_description in location_descriptions:
        connections = {
            direction: locations[name]
            for direction, name in location_description.get("connections", {}).items()
        }
        locations[location_description["name"]].connections = connections
