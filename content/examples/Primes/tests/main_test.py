from primes.__main__ import main


def test_main_function(capsys):
    main(["42"])
    captured = capsys.readouterr()
    assert captured.out == "[2, 3, 7]\n"
