#!/usr/bin/env python3
import math


def nim(x: int, y: int) -> bool:
    if x == y:
        return True
    if x > y:
        # ensure x <= y
        x, y = y, x
    a = (1 + math.sqrt(5)) // 2
    b = (3 + math.sqrt(5)) // 2

    n = 1
    # 这里本来可以用二分搜索的。
    # 但是懒得写了。

    while True:
        X = int(math.floor(a * n))
        Y = int(math.floor(b * n))
        if X == x and Y == y:
            # 落入危险境地
            return False
        elif X > x and Y > y:
            # 成功渡过难关
            return True
        else:
            # 陷入下一个轮回
            n += 1
            pass
