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


@timer.register()
def sum_of_multiples_2():   # optimized function, runs faster
    return sum(num for num in range(1, 1000) if
               num % 3 == 0 or num % 5 == 0)


@timer.register()
def sum_of_multiples_3():   # another optimization
    three = sum(num for num in range(3, 1000, 3))
    five = sum(num for num in range(5, 1000, 5))
    fifteen = sum(num for num in range(15, 1000, 15))
    return three + five - fifteen


timer.run(repeats=10_000, inject_results=True)


### DON'T REMOVE IT ### 0d7eaf6da2897188d0661c8bada15ae4 ###
#
# 'sum_of_multiples':
# 	elapsed time: 3.0s, repeats: 10000, result: 233168
# 'sum_of_multiples_2':
# 	elapsed time: 2.1s, repeats: 10000, result: 233168
# 'sum_of_multiples_3':
# 	elapsed time: 0.627s, repeats: 10000, result: 233168
