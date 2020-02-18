#!/usr/bin/env python

import testcases
from functools import lru_cache


class Solution:
    def __init__(self, volume: int, drinks: list):

        self.volume = volume
        self.drinks = drinks
        self.drink_count = len(self.drinks)
        self.opt = [[0] * (self.drink_count + 1) for _ in range(volume + 1)]

    @lru_cache(maxsize=None)
    def dfs(self, vol: int, typee: int) -> int:

        if typee == self.drink_count:
            if vol >= 0:
                return 0
            return float('-inf')

        if vol < 0:
            return float('-inf')
        elif vol == 0:
            return 0

        current_drink = self.drinks[typee]

        ret = float('-inf')
        for i in range(0, current_drink.max_amount + 1):

            if vol < i * current_drink.volume:
                break
            ret = max(ret, current_drink.satisfactoriness * i + self.dfs(
                vol - i * current_drink.volume, typee + 1))

        return ret


if __name__ == '__main__':
    vol = int(input('volume? >>> '))
    sol = Solution(vol, testcases.drink_list)
    print(sol.dfs(vol, 0))
