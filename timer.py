"""
module used for timing purposes
"""

from functools import wraps as _wraps
from time import perf_counter as _perf_counter


def parameterized_timer(repeats=100_000):
    """a decorator factory used for timing purposes
    default value for repeats is set to 100_000"""
    def timer_decorator(fn):
        @_wraps(fn)
        def inner(*a, **kw):
            start = _perf_counter()
            for n in range(repeats-1):
                fn(*a, **kw)
            result = fn(*a, **kw)
            elapsed_time = _perf_counter() - start
            print(f"elapsed time of '{fn.__name__}': {round(elapsed_time, 3)}s (repeats={repeats})")
            return result
        return inner
    return timer_decorator