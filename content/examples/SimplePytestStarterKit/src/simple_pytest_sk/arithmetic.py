def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def lerp(x, y, t):
    return (1 - t) * x + t * y


def negate(x):
    """Return the negative value of x."""
    return -x


def my_abs(x):
    """Return the absolute value of x."""
    if x <= 0:
        return x
    else:
        return -x
