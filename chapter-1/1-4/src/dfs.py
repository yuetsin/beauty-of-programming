#!/usr/bin/env python

from functools import lru_cache

books = (2, 2, 2, 1, 1)

per_price = 8

discounts = {
    5: 0.25,
    4: 0.2,
    3: 0.1,
    2: 0.05,
    1: 0.0
}

cost = 0.0

get_cost_call_count = 0


def tuple_minus(t1: tuple, t2: tuple) -> tuple:
    assert(len(t1) == len(t2))

    ret = []

    for i in range(len(t1)):
        ret.append(t1[i] - t2[i])

    return tuple(ret)


@lru_cache(maxsize=None)
def get_cost(books: tuple) -> float:
    global get_cost_call_count

    get_cost_call_count += 1

    if books == (0, 0, 0, 0, 0):
        return 0.0

    # exhaust all purchasing ways
    possible = [()]
    for item in books:
        if item > 0:
            possible *= 2

            for i in range(len(possible) // 2):
                possible[i] = possible[i] + (0,)

            for i in range(len(possible) // 2, len(possible)):
                possible[i] = possible[i] + (1,)
        else:
            for i in range(len(possible)):
                possible[i] = possible[i] + (0,)

    min_cost = float('+inf')
    for test in possible:
        if test == (0, 0, 0, 0, 0):
            # avoid self-call deadloop
            continue
        cost = get_cost(tuple_minus(books, test)) + \
            sum(test) * (1 - discounts[sum(test)]) * per_price
        min_cost = min(min_cost, cost)

    return min_cost


print("total price: %.2f" % get_cost(books))
print("called get_cost times: %d" % get_cost_call_count)
