#!/usr/bin/env python3

from random import shuffle, randint
from prettytable import PrettyTable


class Game:

    chessboard: list

    def __init__(self, width: int, height: int, shapes: str):
        # initialize the game

        # chessboard must contains even number grids!
        if not (width >= 4 and height >= 4):
            raise ValueError("chessboard size too small (must >= 4 x 4)")
        if not (width <= 20 and height <= 20):
            raise ValueError("chessboard size too big (must <= 20 x 20)")
        if not (width % 2 == 0 or height % 2 == 0):
            raise ValueError("chessboard must contain even grids")
        if len(shapes) <= 2:
            raise ValueError("no enough shape patterns")

        self.chessboard = [[None] * width for _ in range(height)]

        positions = []
        for i in range(width):
            for j in range(height):
                positions.append((i, j))

        shuffle(positions)
        for i in range(len(positions)):
            if i % 2 == 1:
                continue
            # element count must be even
            j = i + 1
            shape = shapes[randint(0, len(shapes) - 1)]
            self.chessboard[positions[i][1]][positions[i][0]] = shape
            self.chessboard[positions[j][1]][positions[j][0]] = shape

    def shuffle(self):
        height = len(self.chessboard)
        width = len(self.chessboard[0])

        shapes = []
        positions = []

        # randomly shuffles the chessboard
        for i in range(width):
            for j in range(height):
                if self.chessboard[j][i] != None:
                    positions.append((i, j))
                    shapes.append(self.chessboard[j][i])

        shuffle(shapes)
        index = 0
        for i, j in positions:
            self.chessboard[j][i] = shapes[index]
            index += 1

    def is_dead_lock(self) -> bool:
        # check if it's a dead lock situation
        return False

    def is_game_over(self) -> bool:
        # check if the game is over
        for row in self.chessboard:
            for tile in row:
                if tile != None:
                    return False
        return True

    def try_link(self, since: (int, int), till: (int, int)) -> bool:
        # tries to link two grids

        height = len(self.chessboard)
        width = len(self.chessboard[0])

        x_min, x_max = -1, width
        y_min, y_max = -1, height

        def __validate(x: int, y: int) -> bool:
            if x <= x_min or x >= x_max or y <= y_min or y >= y_max:
                return False
            return True

        if since == till:
            return False

        if not __validate(since[0], since[1]):
            raise ValueError("invalid position (%d, %d)" %
                             (since[0], since[1]))

        if not __validate(till[0], till[1]):
            raise ValueError("invalid position (%d, %d)" %
                             (till[0], till[1]))

        if self.chessboard[since[1]][since[0]] == None or self.chessboard[till[1]][till[0]] == None:
            raise ValueError("trying to link a void block")

        if self.chessboard[since[1]][since[0]] != self.chessboard[till[1]][till[0]]:
            raise ValueError("trying to link itself")

        queue = set([since])

        turn_count = 3

        while turn_count > 0:
            for x, y in list(queue):

                def __try_beyond(stepper):
                    nonlocal _x, _y
                    _x, _y = stepper(_x, _y)
                    while True:

                        if _x < x_min or _x > x_max or _y < y_min or _y > y_max:
                            break
                        elif _x == x_min or _x == x_max or _y == y_min or _y == y_max:
                            queue.add((_x, _y))
                        elif self.chessboard[_y][_x] == None:
                            queue.add((_x, _y))
                        else:
                            queue.add((_x, _y))
                            break
                        _x, _y = stepper(_x, _y)
                _x, _y = x, y
                __try_beyond(lambda x, y: (x + 1, y))
                _x, _y = x, y
                __try_beyond(lambda x, y: (x - 1, y))
                _x, _y = x, y
                __try_beyond(lambda x, y: (x, y + 1))
                _x, _y = x, y
                __try_beyond(lambda x, y: (x, y - 1))

            # print("arrivable", queue)
            if till in queue:
                self.chessboard[since[1]][since[0]] = None
                self.chessboard[till[1]][till[0]] = None
                return True

            turn_count -= 1
        return False

    def print_chess(self):
        table = PrettyTable(field_names=[''] + list(
            range(1, len(self.chessboard[0]) + 1)))

        row_idx = ord('A')
        for row in self.chessboard:
            table.add_row([chr(row_idx)] + [pat if pat else '' for pat in row])
            row_idx += 1
        print(table)
