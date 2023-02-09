from collections.abc import Mapping
from typing import Any, Dict, List, Optional

from .game import Game
from .pawn import Pawn
from .player import Player
from .world import World, LocationDict
from .location import Location, LocationDescriptions


class GameFactory:
    def __init__(self, object_descriptions: Dict[str, Any] = None, object_classes=None):
        self.object_descriptions: Dict[str, Any] = (
            {} if object_descriptions is None else object_descriptions
        )
        self.object_classes: Dict[str, type] = (
            {} if object_classes is None else object_classes
        )
        self.objects = {}
        self.world: Optional[World] = None
        self.players = {}

    def create_game(
        self, location_descriptions: LocationDescriptions, player_descriptions
    ) -> Game:
        world = self.create_world(location_descriptions)
        players = self.create_players(player_descriptions)
        return Game(players=players, world=world)

    def create_players(self, player_descriptions) -> List[Player]:
        return [self.create_player(desc) for desc in player_descriptions]

    def create_player(self, player_description) -> Player:
        assert self.world is not None
        if not isinstance(player_description, Mapping):
            player_description = {"name": player_description}
        player_name = player_description["name"]
        if self.players.get(player_name) is None:
            location_name = player_description.get("location")
            if location_name is None:
                location_name = self.world.initial_location_name
            self.players[player_name] = Player(
                name=player_description["name"],
                pawn=Pawn(location=self.world[location_name]),
            )
        return self.players[player_name]

    def create_world(
        self,
        location_descriptions: LocationDescriptions,
    ) -> World:
        """Create a World from a description of its locations.

        >>> GameFactory({}).create_world([{"name": "A", "connections": {"east": "B"}},
        ...                               {"name": "B", "connections": {"west": "A"}}])
        World(locations={'A': Location(name='A', connections={'east': ...}),
                             'B': Location(name='B', connections={'west': ...})},
              initial_location_name='A')
        """
        if self.world is None:
            locations = GameFactory._create_locations(location_descriptions)
            self.world = World(
                locations=locations,
                initial_location_name=location_descriptions[0]["name"],
            )
            return self.world
        else:
            raise ValueError("The world has already been created.")

    def create_object(self, object_name):
        """Create an object from the stored object descriptions.

        >>> objs = {"My List": {"class_name": "A Python List", "args": [[1, 2, 3]]}}
        >>> f = GameFactory(objs, {"A Python List": list})
        >>> f.create_object("My List")
        [1, 2, 3]
        """
        if self.objects.get(object_name) is None:
            object_description = self.object_descriptions[object_name]
            object_class = self.object_classes[object_description["class_name"]]
            self.objects[object_name] = object_class(
                *object_description.get("args", []),
                **object_description.get("kwargs", {})
            )
        return self.objects.get(object_name)

    @staticmethod
    def _create_locations(
        location_descriptions: LocationDescriptions,
    ) -> LocationDict:
        """Create a location dictionary from descriptions.

        >>> GameFactory._create_locations(
        ...         [{"name": "A", "connections": {"east": "B"}},
        ...          {"name": "B", "connections": {"west": "A"}}])
        {'A': Location(name='A', connections={'east': Location(name='B', ...)}),
         'B': Location(name='B', connections={'west': Location(name='A', ...)})}
        """
        locations = GameFactory._create_locations_without_connections(
            location_descriptions
        )
        GameFactory._build_connections_for_all_locations(
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
