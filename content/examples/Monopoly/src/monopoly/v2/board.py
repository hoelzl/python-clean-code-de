from dataclasses import dataclass, field
from .square import (
    make_square,
    DrawCardSquare,
    GoSquare,
    GoToJailSquare,
    IncomeTaxSquare,
    RegularSquare,
    Square,
)

SQUARE_DESCRIPTIONS = [
    {"name": "Go", "cls": GoSquare},
    {"name": "Mediterranean Avenue", "cls": RegularSquare},
    {"name": "Community Chest", "cls": DrawCardSquare},
    {"name": "Baltic Avenue", "cls": RegularSquare},
    {"name": "Income Tax", "cls": IncomeTaxSquare},
    {"name": "Reading Railroad", "cls": RegularSquare},
    {"name": "Oriental Avenue", "cls": RegularSquare},
    {"name": "Chance", "cls": DrawCardSquare},
    {"name": "Vermont Avenue", "cls": RegularSquare},
    {"name": "Connecticut Avenue", "cls": RegularSquare},
    {"name": "In Jail/Just Visiting", "cls": RegularSquare},
    {"name": "St. Charles Place", "cls": RegularSquare},
    {"name": "Electric Company", "cls": RegularSquare},
    {"name": "States Avenue", "cls": RegularSquare},
    {"name": "Virginia Avenue", "cls": RegularSquare},
    {"name": "Pennsylvania Railroad", "cls": RegularSquare},
    {"name": "St. James Place", "cls": RegularSquare},
    {"name": "Community Chest", "cls": DrawCardSquare},
    {"name": "Tennessee Avenue", "cls": RegularSquare},
    {"name": "New York Avenue", "cls": RegularSquare},
    {"name": "Free Parking", "cls": RegularSquare},
    {"name": "Kentucky Avenue", "cls": RegularSquare},
    {"name": "Chance", "cls": DrawCardSquare},
    {"name": "Indiana Avenue", "cls": RegularSquare},
    {"name": "Illinois Avenue", "cls": RegularSquare},
    {"name": "B. & O. Railroad", "cls": RegularSquare},
    {"name": "Atlantic Avenue", "cls": RegularSquare},
    {"name": "Ventnor Avenue", "cls": RegularSquare},
    {"name": "Water Works", "cls": RegularSquare},
    {"name": "Marvin Gardens", "cls": RegularSquare},
    {"name": "Go To Jail", "cls": GoToJailSquare},
    {"name": "Pacific Avenue", "cls": RegularSquare},
    {"name": "North Carolina Avenue", "cls": RegularSquare},
    {"name": "Community Chest", "cls": DrawCardSquare},
    {"name": "Pennsylvania Avenue", "cls": RegularSquare},
    {"name": "Short Line", "cls": RegularSquare},
    {"name": "Chance", "cls": DrawCardSquare},
    {"name": "Park Place", "cls": RegularSquare},
    {"name": "Luxury Tax", "cls": RegularSquare},
    {"name": "Boardwalk", "cls": RegularSquare},
]


def _create_squares():
    squares = [
        make_square(index=index, **square_description)
        for index, square_description in enumerate(SQUARE_DESCRIPTIONS)
    ]
    assert len(squares) == 40
    return squares


@dataclass
class Board:
    """A representation of the Monopoly board.

    >>> Board()
    Board(squares=[GoSquare(name='Go', index=0),
                   RegularSquare(name='Mediterranean Avenue', index=1), ...])
    """

    squares: list[Square] = field(default_factory=_create_squares)

    def __getitem__(self, item) -> Square:
        """Return a Square by name or index.

        >>> Board()[0]
        GoSquare(name='Go', index=0)
        >>> Board()["Go"]
        GoSquare(name='Go', index=0)
        """
        if isinstance(item, str):
            return self.get_square_by_name(item)
        else:
            return self.get_square_by_index(item)

    def get_square_by_name(self, name):
        """Return the square with a given name.

        >>> Board().get_square_by_name("St. Charles Place")
        RegularSquare(name='St. Charles Place', index=11)
        >>> Board().get_square_by_name("5th Avenue") is None
        True
        """
        for square in self.squares:
            if square.name == name:
                return square
        return None

    def get_square_by_index(self, index) -> Square:
        """Return the square for a given index.

        >>> Board().get_square_by_index(0)
        GoSquare(name='Go', index=0)
        """
        return self.squares[index]

    def get_square_by_offset(self, location, offset):
        """Get a square at an offset to location.

        >>> b = Board()
        >>> go = b[0]
        >>> b.get_square_by_offset(go, 11)
        RegularSquare(name='St. Charles Place', index=11)

        After 40 moves we return to the original square.

        >>> b.get_square_by_offset(go, 40)
        GoSquare(name='Go', index=0)
        >>> b.get_square_by_offset(go, 51)
        RegularSquare(name='St. Charles Place', index=11)
        """
        new_index = (location.index + offset) % len(self.squares)
        return self.squares[new_index]
