def fizzbuzz(n: int) -> None:
    """Print the FizzBuzz numbers from 1 to n to the screen."""
    print(fizzbuzz_str(n))


def fizzbuzz_str(n: int) -> str:
    """Return the FizzBuzz output from 1 to n as string.

    >>> fizzbuzz_str(6)
    '1\\n2\\nFizz\\n4\\nBuzz\\nFizz'
    """
    return "\n".join(fizzbuzz_numbers(n))


def fizzbuzz_numbers(n: int) -> list[str]:
    """Create a list of FizzBuzz numbers from 1 to n.

    >>> fizzbuzz_numbers(6)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz']
    """
    return [fizzbuzz_number(i) for i in range(1, n + 1)]


def fizzbuzz_number(n: int) -> str:
    """Converts a single number to a string following the FizzBuzz rules.

    >>> fizzbuzz_number(1)
    '1'
    >>> fizzbuzz_number(3)
    'Fizz'
    >>> fizzbuzz_number(5)
    'Buzz'
    >>> fizzbuzz_number(15)
    'FizzBuzz'
    """
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result or str(n)
