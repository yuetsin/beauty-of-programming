#!/usr/bin/env python

from time import time
from functools import lru_cache

stone_count = int(input("Stone Count N = ? >>> "))


start_time = time()

stones = tuple(range(1, stone_count + 1))

# 注意对于每个玩家而言，
# 如果所有可能的操作最终都指向输，那么这一步就完全输
# 但只要有一步可能的操作指向赢，那么这一步就可以赢


@lru_cache(maxsize=None)
def canWin(stones: tuple) -> bool:
    if len(stones) == 1:
        # One single stone left
        return True
    elif len(stones) == 2 and stones[0] + 1 == stones[1]:
        # Two consecutive stones left
        return True

    iCanWin = False
    for i in range(len(stones)):
        left_stones = stones[:i] + stones[i + 1:]
        # 这里的 canWin 指的是对手
        if not canWin(left_stones):
            iCanWin = True
            break

    if iCanWin:
        return True

    for i in range(len(stones) - 1):
        # find consecutive stones
        if stones[i] + 1 == stones[i + 1]:
            left_stones = stones[:i] + stones[i + 2:]
            if not canWin(left_stones):
                iCanWin = True
                breakpoint

    return iCanWin


iCanWin = canWin(stones)

end_time = time()
print(iCanWin)
print("Time elapsed: ", end_time - start_time, "seconds")
