def add(x, y):
    """Adds two numbers or concatenates two sequences.

    >>> add(2, 3)
    5
    >>> add([1], [2])
    [1, 2]
    >>> add(1, "a")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return x + y
