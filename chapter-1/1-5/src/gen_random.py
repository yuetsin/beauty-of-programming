#!/usr/bin/env python

import random

# N = 1e9

N = int(input('N = ? >>>'))

loss_num = random.randint(1, N)
loss_machine = random.randint(0, 1) == 0

M1 = list(range(N))
M2 = list(range(N))

if loss_machine:
    M1.remove(loss_num)
else:
    M2.remove(loss_num)

random.shuffle(M1)
random.shuffle(M2)

with open('machine1.rb', 'w') as f1:
    f1.write('\n'.join([str(i) for i in M1]))

with open('machine2.rb', 'w') as f2:
    f2.write('\n'.join([str(i) for i in M2]))

print('ok')
