"""
module used for timing purposes
"""

from functools import wraps as _wraps
from time import perf_counter as _perf_counter
import inspect as _inspect
import re as _re
import os as _os
import hashlib as _hashlib


def hash_it(string, *, algorithm="sha256"):
    """
    returns a hash (=digest) of provided string
    default algorithm is sha256
    """
    algo = getattr(_hashlib, algorithm, None)
    if algo is None:
        raise AttributeError(f"Algorithm '{algorithm}' does not exist")
    m = algo()
    m.update(bytearray(string, encoding="utf-8"))
    return m.hexdigest()


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


class timer:
    """
    timer aimed for comparing runtime of different functions

    usage:
        1) register a function you want to time with @register()
            - if decorated function takes arguments, they must be provided as parameters to @register()
            - if decorated function has default values, they can be overwritten by providing arguments to @register()

        2) after all functions are registered, perform timing with 'timer.run()'
            - number of iterations can be specified, default is 'timer.run(repeats=1_000)
            - results can be directly injected to the end of working file with 'time.run(inject_results=True)'
    """

    _registry = {}
    _registry_hash = None

    @classmethod
    def register(cls, *arg):
        def inner(fn):
            cls._registry[fn] = arg or fn.__defaults__ or ()
            cls._registry_hash = cls._hash_registry_content()
            return fn
        return inner

    @classmethod
    def run(cls, repeats=1_000, *, inject_results=False):
        results_to_be_injected = []

        for fn, params in cls._registry.items():
            fn_run_result = cls._timer(fn, repeats, *params)
            print(fn_run_result)

            if inject_results:
                results_to_be_injected.append(fn_run_result)

        if inject_results is True:
            # ↓↓↓ extracts path to file to which results of timing will be injected
            obj = str(_inspect.getmembers(fn)[4][1])
            file_path = _re.search(r'"(.*)"', obj).group(1)

            # ↓↓↓ injects result of timing to the working file
            with open(file_path, "r+") as file:
                file.seek(0, _os.SEEK_END)
                file.write(f"\n\n### DON'T REMOVE IT ### {timer._registry_hash} ###\n#\n")

                for r in results_to_be_injected:
                    splitted = r.split("\n")
                    new_string = "".join(["# "+s+"\n" for s in splitted if s != ""])
                    file.write(new_string)
        return

    @staticmethod
    def _timer(fn, repeats, *arg):
        def inner(arg):
            start = _perf_counter()
            for n in range(repeats - 1):
                fn(*arg)
            result = fn(*arg)
            elapsed_time = _perf_counter() - start

            res_string = [
                f"'{fn.__qualname__}':\n\t", f"elapsed time: {elapsed_time:.3}s, ",
                f"repeats: {repeats}, ", f"result: {result}\n"]
            return "".join(res_string)
        return inner(arg)

    @classmethod
    def _hash_registry_content(cls):
        content_to_hash = []
        for k, v in cls._registry.items():
            content_to_hash.append(str(k.__qualname__))
            content_to_hash.append(str(v))
        return hash_it("".join(content_to_hash), algorithm="md5")
