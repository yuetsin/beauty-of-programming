#!/usr/bin/env python

from testcases import gen_random, gen_fake_random
from time import time

begin = time()


RANDOM = True


conf_cnt = 8

if RANDOM:
    test_cases = gen_random(10, conf_cnt)
else:
    test_cases = gen_fake_random()


def check_valid(colors: list) -> bool:
    # check if it's a valid palette
    for conflicts in test_cases:
        results = [colors[i] for i in conflicts]
        if len(set(results)) != len(conflicts):
            # conflict exists!
            return False

    return True


def get_color_count(colors: list) -> int:
    # get different color counts in a palette
    return len(set(colors))


palettes = [[0]]

for _ in range(1, conf_cnt):
    new_palettes = []

    for palette in palettes:
        for i in range(conf_cnt):
            new_palettes.append(palette + [i])

    palettes = new_palettes

min_color = conf_cnt
min_palette = []

for palette in palettes:
    color_count = get_color_count(palette)
    if color_count > min_color:
        continue

    if not check_valid(palette):
        continue

    if color_count < min_color:
        min_color = color_count
        min_palette = [palette]
    elif color_count == min_color:
        min_palette.append(palette)

end = time()

print("Min color count: %d" % min_color)
print("Possible coloring palettes: \n%s" %
      ('\n'.join([str(p) for p in min_palette])))
print("Min color count: %d" % min_color)
print("\nTime elapsed: %.6fs" % (end - begin))
