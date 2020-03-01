#!/usr/bin/env python

from functools import lru_cache
from collections import Counter
from testcases import gen_requests

reqs = gen_requests(False)

counter = dict(Counter(reqs))


@lru_cache(maxsize=None)
def __wrapped_counter(i: int) -> int:
    if i in counter:
        return counter[i]

    return 0


max_floor = max(reqs)
min_floor = min(reqs)

min_costs = 0
target_floor = None

n1, n2, n3 = 0, 0, 0

for i in range(min_floor, max_floor + 1):
    n2 += __wrapped_counter(i)
    min_costs += __wrapped_counter(i) * (i - 1)

for i in range(min_floor, max_floor + 1):
    if n1 + n3 < n2:
        target_floor = i
        min_costs += (n1 + n3 - n2)
        n1 += n3
        n2 -= __wrapped_counter(i)
        n3 = __wrapped_counter(i)
    else:
        break

print("floor #%d. min costs: %d" % (target_floor, min_costs))
