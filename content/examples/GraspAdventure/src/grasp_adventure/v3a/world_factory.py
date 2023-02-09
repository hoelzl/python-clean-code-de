from .world import World, LocationDict
from .location import Location, LocationDescriptions


class LevelFactory:
    @staticmethod
    def create(
        location_descriptions: LocationDescriptions,
    ) -> World:
        """Create a World from a description of its locations.

        >>> LevelFactory().create([{"name": "A", "connections": {"east": "B"}},
        ...                        {"name": "B", "connections": {"west": "A"}}])
        World(locations={'A': Location(name='A', connections={'east': ...}),
                             'B': Location(name='B', connections={'west': ...})},
             initial_location_name='A')
        """
        return World(
            locations=(LevelFactory._create_locations(location_descriptions)),
            initial_location_name=location_descriptions[0]["name"],
        )

    @staticmethod
    def _create_locations(
        location_descriptions: LocationDescriptions,
    ) -> LocationDict:
        """Create a location dictionary from descriptions.

        >>> LevelFactory._create_locations(
        ...         [{"name": "A", "connections": {"east": "B"}},
        ...          {"name": "B", "connections": {"west": "A"}}])
        {'A': Location(name='A',
              connections={'east': Location(name='B', connections={'west': ...})}),
         'B': Location(name='B',
              connections={'west': Location(name='A', connections={'east': ...})})}
        """
        locations = LevelFactory._create_locations_without_connections(
            location_descriptions
        )
        LevelFactory._build_connections_for_all_locations(
            locations, location_descriptions
        )
        return locations

    @staticmethod
    def _create_locations_without_connections(
        location_descriptions: LocationDescriptions,
    ) -> LocationDict:
        locations = {
            location_description["name"]: Location(location_description["name"])
            for location_description in location_descriptions
        }
        return locations

    @staticmethod
    def _build_connections_for_all_locations(
        locations: LocationDict, location_descriptions: LocationDescriptions
    ):
        for location_description in location_descriptions:
            connections = {
                direction: locations[name]
                for direction, name in location_description.get(
                    "connections", {}
                ).items()
            }
            locations[location_description["name"]].connections = connections
