"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from timer import timer
from math import floor, sqrt
import itertools

#TODO: implement proper data structure for keeping prime factors in sorted manner


def generate_primes():
    # ↓↓↓ yields predefined prime numbers
    predefined = (2, 3, 5, 7)
    yield from predefined

    # we are interested only in yielding numbers ending with digit 1, 3, 7 or 9
    # ↓↓↓ if incremented from number 11, it will not yield any number divisible by 5
    increment = itertools.cycle((2, 4, 2, 2))
    num = 11

    # ↓↓↓ yields calculated prime numbers
    while True:
        # ↓↓↓ 'for else' construct → else clause is executed only if for loop is exited without break
        for d in range(2, floor(sqrt(num)) + 1):
            if num % d == 0:
                num += next(increment)
                break
        else:
            yield num
            num += next(increment)


def largest_prime_factor(num: int) -> int:
    pass