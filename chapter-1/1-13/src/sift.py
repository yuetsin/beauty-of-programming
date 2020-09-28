#!/usr/bin/env python3


def nim(x: int, y: int) -> bool:
    if x == y:
        return True

    if x > y:
        # make sure x <= y
        x, y = y, x

    if x == 1 and y == 2:
        # basic failure situation
        return False

    known = set()
    known.add(2)

    n = 1
    delta = 1

    while x > n:
        n += 1
        while n in known:
            n += 1
        delta += 1
        known.add(n + delta)

    if x != y - n + 1:
        return True

    if not y in known:
        return True

    return False
