from dataclasses import dataclass
from io import StringIO
from typing import List

from .player import Player
from .world import World


@dataclass
class Game:
    players: List[Player]
    world: World

    @property
    def description(self):
        io = StringIO()
        for player in self.players:
            print(player.description, file=io)
        print(self.world.description, file=io)
        return io.getvalue()

    def play_round(self):
        for player in self.players:
            player.take_turn()
        self.print_round_header()
        print(self.description)

    def print_round_header(self):
        header = "Playing a round."
        print()
        print(header)
        print("=" * len(header))
        print()
