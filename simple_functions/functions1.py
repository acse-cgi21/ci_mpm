from functools import lru_cache


__all__ = ['my_sum', 'factorial', 'my_sin']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    return n * factorial(n-1) if n else 1


def my_sin(x):
    my_sin = 0
    i = 2
    for n in range(1, 1000, 2):
        my_sin += x**n / factorial(n) * (-1)**i
        i += 1
    return my_sin
