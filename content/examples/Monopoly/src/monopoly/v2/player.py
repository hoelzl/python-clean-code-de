import random
from enum import Enum
from typing import TYPE_CHECKING

from .die import Die

if TYPE_CHECKING:
    from .monopoly_game import MonopolyGame


class PieceName(str, Enum):
    TOP_HAT = "Top Hat"
    THIMBLE = "Thimble"
    IRON = "Iron"
    SHOE = "Shoe"
    BATTLESHIP = "Battleship"
    CANNON = "Cannon"
    RACE_CAR = "Race Car"
    PURSE = "Purse"
    ROCKING_HORSE = "Rocking Horse"
    LANTERN = "Lantern"


class Player:
    def __init__(self, name: str, piece: PieceName, game: "MonopolyGame"):
        self.name = name
        self.piece = piece
        self.game = game
        self._location = self.game.board["Go"]
        self._die = Die()

    def __repr__(self):
        return (
            f"{type(self).__name__}(name={self.name!r}, piece={self.piece!r}, "
            f"location={self.location!r})"
        )

    def __str__(self):
        return f"Player {self.name} ({self.piece}, {self.location})"

    @property
    def location(self):
        """Return the location of the player."""
        return self._location

    @location.setter
    def location(self, new_location):
        """Set the location of the player and notify the location."""
        new_location.landed_on(self)
        self._location = new_location

    def take_turn(self):
        """Take a single turn.

        >>> from monopoly.v2.monopoly_game import MonopolyGame
        >>> p = MonopolyGame(1).players[0]
        >>> random.seed(1)
        >>> p
        Player(name='Player 1',
            piece=<PieceName.TOP_HAT: 'Top Hat'>,
            location=GoSquare(name='Go', index=0))
        >>> p.take_turn()
        >>> p
        Player(name='Player 1',
            piece=<PieceName.TOP_HAT: 'Top Hat'>,
            location=DrawCardSquare(name='Chance', index=7))
        """
        dice_roll = self._die.roll() + self._die.roll()
        new_location = self.game.board.get_square_by_offset(self.location, dice_roll)
        new_location.landed_on(self)
        self.location = new_location
