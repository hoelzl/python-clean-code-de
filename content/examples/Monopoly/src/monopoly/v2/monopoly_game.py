from collections.abc import Sequence
from dataclasses import dataclass, field

from monopoly.v2.board import Board
from monopoly.v2.player import PieceName, Player


@dataclass
class MonopolyGame:
    num_players: int
    board: Board = field(default_factory=Board, repr=False)
    players: Sequence[Player] = field(init=False)

    def __post_init__(self):
        """Finish initialization of MonopolyGanme.

        >>> MonopolyGame(2)
        MonopolyGame(num_players=2,
            players=[Player(name='Player 1',
                        piece=<PieceName.TOP_HAT: 'Top Hat'>,
                        location=GoSquare(name='Go', index=0)),
                     Player(name='Player 2',
                        piece=<PieceName.THIMBLE: 'Thimble'>,
                        location=GoSquare(name='Go', index=0))])
        """
        go_square = self.board["Go"]
        self.players = [
            Player(f"Player {i + 1}", piece_name, self)
            for i, piece_name in zip(range(self.num_players), PieceName)
        ]
