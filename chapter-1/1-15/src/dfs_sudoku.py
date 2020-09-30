#!/usr/bin/env python3

from random import shuffle
from prettytable import PrettyTable


def __validate_block(block: list) -> bool:
    for i in range(1, 10):
        if block.count(i) > 1:
            return False
    return True


def validate_sudoku(grid: list) -> bool:
    for i in range(9):
        if not __validate_block(grid[i * 9:(i + 1) * 9]):
            # print("invalid: row", i, "not good")
            return False

    for i in range(9):
        cols = []
        for j in range(9):
            cols.append(grid[j * 9 + i])
        if not __validate_block(cols):
            # print("invalid: column", i, "not good")
            return False

    for i in range(3):
        for j in range(3):
            block = []
            for offset in range(3):
                block += grid[(i * 3 + offset) * 9 + j *
                              3: (i * 3 + offset) * 9 + (j + 1) * 3]
            if not __validate_block(block):
                # print("invalid: block", i, j, "not good")
                return False

    return True


def print_sudoku(grid: list):
    sudoku = PrettyTable(
        field_names=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
    for i in range(9):
        sudoku.add_row(grid[i * 9:(i + 1) * 9])
    print(sudoku)


def get_random_chain(typ: str = 'random') -> list:
    if typ == 'random':
        l = list(range(1, 10))
        shuffle(l)
        return l
    elif typ == 'min':
        return list(range(1, 10))
    elif typ == 'max':
        return list(range(9, 0, -1))
    else:
        return [1, 4, 7, 2, 5, 8, 3, 6, 9]


def generate_sudoku_dfs() -> list:
    sudoku = [0] * 81

    def __generate_sudoku(at: int) -> bool:
        if at >= 81:
            return True
        for i in get_random_chain():
            sudoku[at] = i
            # print("current sudoku:", sudoku)
            if validate_sudoku(sudoku) and __generate_sudoku(at + 1):
                # print("set", at, "to", i)
                return True
            sudoku[at] = 0

        return False

    __generate_sudoku(0)
    return sudoku
