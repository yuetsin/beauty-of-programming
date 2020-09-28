#!/usr/bin/env python3

from functools import lru_cache


# cache size won't exceed N * M
@lru_cache(maxsize=None)
def nim(n: int, m: int) -> bool:
    if n == 0 and m == 0:
        # this case might never be reached
        return False
    elif n == 0 or m == 0:
        return True
    elif n == m:
        return True
    else:
        for take_n in range(1, n):
            if not nim(n - take_n, m):
                return True

        for take_m in range(1, m):
            if not nim(n, m - take_m):
                return True

        for take_both in range(1, min(n, m)):
            if not nim(n - take_both, m - take_both):
                return True

        return False
