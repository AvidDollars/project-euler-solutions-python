"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

from timer import timer


@timer.register()
def sum_of_multiples(rng=(1, 1000), multiples=(3, 5)):
    final_sum = 0
    for num in range(*rng):
        for m in multiples:
            if num % m == 0:
                final_sum += num
                break
    return final_sum


@timer.register()       # optimized function, runs faster
def sum_of_multiples_2():
    return sum(num for num in range(1, 1000) if
               num % 3 == 0 or num % 5 == 0)


timer.run(repeats=5000)