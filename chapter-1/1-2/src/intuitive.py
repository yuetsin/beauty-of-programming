#!/usr/bin/env python

shared_x = ['d', 'e', 'f']

jiang_y = ['8', '9', '10']

shuai_y = ['1', '2', '3']

for s_x in shared_x:
    for j_x in shared_x:
        if j_x == s_x:
            continue

        for s_y in shuai_y:
            for j_y in jiang_y:
                print('將：(%s, %s)，帥：(%s, %s)' % (j_x, j_y, s_x, s_y))

