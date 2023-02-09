from simple_packaging.greeting import say_hi


def test_say_hi_with_default_args(capsys):
    say_hi()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"


def test_say_hi_with_name_arg(capsys):
    say_hi(name="John")
    captured = capsys.readouterr()
    assert captured.out == "Hello, John!\n"
