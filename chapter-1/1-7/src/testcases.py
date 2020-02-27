#!/usr/bin/env python

from random import random, randint
from light import Light


def build_cases() -> list:

    cases = []

    line_count = randint(5, 20)

    for _ in range(line_count):
        cases.append(Light(random(), random(), random()))

    return cases
