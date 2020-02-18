#!/usr/bin/env python

import testcases


class Solution:

    def __init__(self, volume: int, drinks: list):

        self.volume = volume
        self.drinks = drinks
        self.drink_count = len(self.drinks)
        self.opt = [[0] * (self.drink_count + 1) for _ in range(volume + 1)]

    def calculate(self) -> int:

        for j in range(0, self.drink_count + 1):
            self.opt[0][j] = 0

        for j in range(self.drink_count - 1, -1, -1):
            # print('handling %s' % (str(self.drinks[j])))
            for i in range(0, self.volume + 1):

                for k in range(0, self.drinks[j].max_amount + 1):
                    if i < k * self.drinks[j].volume:
                        break

                    x = self.opt[i - k * self.drinks[j].volume][j +
                                                                1] + self.drinks[j].satisfactoriness * k
                    if x > self.opt[i][j]:
                        self.opt[i][j] = x

        return self.opt[self.volume][0]


if __name__ == '__main__':
    vol = int(input('volume? >>> '))
    sol = Solution(vol, testcases.drink_list)
    print(sol.calculate())
    # print(sol.opt)
