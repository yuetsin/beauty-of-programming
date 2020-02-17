#!/usr/bin/env python

with open('machine1.rb', 'r') as f1:
    m1 = f1.read().split('\n')

with open('machine2.rb', 'r') as f2:
    m2 = f2.read().split('\n')

visited = set()

result = 0
for idx in m1 + m2:
    result ^= int(idx)

print('unique id: ')
print(result)
