from monopoly.v2.monopoly_game import MonopolyGame


def test_monopoly_game():
    game = MonopolyGame(4)

    assert len(game.players) == 4
    assert len(game.board.squares) == 40
