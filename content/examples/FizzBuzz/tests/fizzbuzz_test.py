from fizzbuzz.fizzbuzz import fizzbuzz_number, fizzbuzz_numbers, fizzbuzz_str


def test_fizzbuzz_number():
    assert fizzbuzz_number(1) == "1"
    assert fizzbuzz_number(3) == "Fizz"
    assert fizzbuzz_number(5) == "Buzz"
    assert fizzbuzz_number(6) == "Fizz"
    assert fizzbuzz_number(15) == "FizzBuzz"


FIZZBUZZ_RESULTS = [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz",
    "16",
]


def test_fizzbuzz_numbers():
    assert fizzbuzz_numbers(16) == FIZZBUZZ_RESULTS


def test_fizzbuzz_str():
    assert fizzbuzz_str(16) == "\n".join(FIZZBUZZ_RESULTS)
