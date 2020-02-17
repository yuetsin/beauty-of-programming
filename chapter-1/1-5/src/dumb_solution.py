#!/usr/bin/env python

with open('machine1.rb', 'r') as f1:
    m1 = f1.read().split('\n')

with open('machine2.rb', 'r') as f2:
    m2 = f2.read().split('\n')

visited = set()
unique = set()

for idx in m1 + m2:
    if idx in visited and idx in unique:
        unique.remove(idx)
    else:
        visited.add(idx)
        unique.add(idx)

print('unique id(s): ')
print(unique)
