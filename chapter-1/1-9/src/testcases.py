#!/usr/bin/env python

from random import randint


def gen_random(student_cnt: int, conference_cnt: int) -> list:
    results = []

    for _ in range(student_cnt):
        conferences = set()

        for _ in range(randint(2, 4)):
            conferences.add(randint(0, conference_cnt - 1))

        results.append(sorted(list(conferences)))

    return results


def gen_fake_random() -> list:
    return [[0, 6], [0, 6, 7], [2, 6], [1, 7], [0, 5, 6], [0, 5, 7], [0, 5, 6], [0, 4, 6, 7]]
