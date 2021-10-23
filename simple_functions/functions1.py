from functools import lru_cache


__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot
