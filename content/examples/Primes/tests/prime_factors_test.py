from primes.prime_factors import compute_prime_factors


def test_prime_factors_of_2():
    assert compute_prime_factors(2) == [2]


def test_prime_factors_of_3():
    assert compute_prime_factors(3) == [3]


def test_prime_factors_of_4():
    assert compute_prime_factors(4) == [2, 2]


def test_prime_factors_of_5():
    assert compute_prime_factors(5) == [5]


def test_prime_factors_of_1():
    assert compute_prime_factors(1) == []
