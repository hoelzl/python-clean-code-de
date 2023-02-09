from typing import List


def compute_prime_factors(n: int) -> List[int]:
    """Compute the prime factors of a positive integer.

    >>> compute_prime_factors(2)
    [2]
    >>> compute_prime_factors(12)
    [2, 2, 3]
    >>> compute_prime_factors(1)
    []
    """
    result = []
    for factor in range(2, n + 1):
        while n % factor == 0:
            result.append(factor)
            n /= factor
    return result
