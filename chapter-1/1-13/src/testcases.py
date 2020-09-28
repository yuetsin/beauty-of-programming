#!/usr/bin/env python3

from prettytable import PrettyTable

sol = 'math'


if sol == 'idiot':
    from idiot import nim
elif sol == 'sift':
    from sift import nim
elif sol == 'math':
    from mathh import nim
else:
    exit(-1)


N = 14
M = 17

x = PrettyTable()
x.field_names = ['n\\m'] + list(range(1, M + 1))

for n in range(1, N + 1):
    row = [n]
    for m in range(1, M + 1):
        if m >= n:
            row.append('W' if nim(n, m) else 'L')
        else:
            row.append('-')
    x.add_row(row)


print("this table is generated by %s solution" % sol)
print(x)