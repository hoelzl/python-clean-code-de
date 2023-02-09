from dataclasses import dataclass, field


@dataclass
class Square:
    name: str


SQUARE_NAMES = [
    "Go",
    "Mediterranean Avenue",
    "Community Chest",
    "Baltic Avenue",
    "Income Tax",
    "Reading Railroad",
    "Oriental Avenue",
    "Chance",
    "Vermont Avenue",
    "Connecticut Avenue",
    "In Jail/Just Visiting",
    "St. Charles Place",
    "Electric Company",
    "States Avenue",
    "Virginia Avenue",
    "Pennsylvania Railroad",
    "St. James Place",
    "Community Chest",
    "Tennessee Avenue",
    "New York Avenue",
    "Free Parking",
    "Kentucky Avenue",
    "Chance",
    "Indiana Avenue",
    "Illinois Avenue",
    "B. & O. Railroad",
    "Atlantic Avenue",
    "Ventnor Avenue",
    "Water Works",
    "Marvin Gardens",
    "Go To Jail",
    "Pacific Avenue",
    "North Carolina Avenue",
    "Community Chest",
    "Pennsylvania Avenue",
    "Short Line",
    "Chance",
    "Park Place",
    "Luxury Tax",
    "Boardwalk",
]


def _create_squares():
    squares = [Square(name) for name in SQUARE_NAMES]
    assert len(squares) == 40
    return squares


@dataclass
class Board:
    """A representation of the Monopoly board.

    >>> Board()
    Board(squares=[Square(name='Go'), Square(name='Mediterranean Avenue'), ...])
    """

    squares: list[Square] = field(default_factory=_create_squares)

    def get_square(self, name):
        """Return the square with a given name.

        >>> Board().get_square("St. Charles Place")
        Square(name='St. Charles Place')
        >>> Board().get_square("5th Avenue") is None
        True
        """
        for square in self.squares:
            if square.name == name:
                return square
        return None
