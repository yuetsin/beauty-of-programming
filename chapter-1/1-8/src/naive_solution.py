#!/usr/bin/env python

from testcases import gen_requests

reqs = gen_requests(False)

min_floor = None
min_costs = float('+inf')

for floor in range(min(reqs), max(reqs) + 1):
    # try taking them all to floor #i
    costs = sum([abs(i - floor) for i in reqs])
    if costs < min_costs:
        min_costs = costs
        min_floor = floor

print("floor #%d. min costs: %d" % (min_floor, min_costs))
