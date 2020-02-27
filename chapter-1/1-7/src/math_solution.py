#!/usr/bin/env python

from testcases import build_cases
from exceptions import NoSolutionException, InfiniteSolutionException


cases = build_cases()

points = []

for idx, line1 in enumerate(cases):
    for _, line2 in enumerate(cases[idx + 1:]):
        try:
            points.append(line1.intersect(line2))
        except NoSolutionException:
            pass
        except InfiniteSolutionException:
            print("Invalid test case!")
            assert(0)

print("Cases: ")
print(cases)

print("Intersecting Points: ")
print(points)

while True:
    a = float(input("a = ? >>> "))
    b = float(input("b = ? >>> "))

    assert(a < b)

    count = 1 + len(cases)

    for p in points:
        if a < p[0] < b:
            count += 1

    print("result: %d~" % count)
