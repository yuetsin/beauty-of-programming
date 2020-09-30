#!/usr/bin/env python3

from random import shuffle
from prettytable import PrettyTable


def validate_block(block: list) -> bool:
    for i in range(1, 10):
        if not i in block:
            return False
        return True


def validate_sudoku(grid: list) -> bool:
    for i in range(9):
        if not validate_block(grid[i * 9:(i + 1) * 9]):
            return False

    for i in range(9):
        cols = []
        for j in range(9):
            cols.append(grid[j * 9 + i])
        if not validate_block(cols):
            return False

    for i in range(3):
        for j in range(3):
            block = []
            for offset in range(3):
                block += grid[(i * 3 + offset) * 9 + j *
                              3: (i * 3 + offset) * 9 + (j + 1) * 3]
            print(block)
            if not validate_block(block):
                return False

    return True


def print_sudoku(grid: list):
    sudoku = PrettyTable(
        field_names=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
    for i in range(9):
        sudoku.add_row(grid[i * 9:(i + 1) * 9])
    print(sudoku)


def generate_sudoku_insane() -> list:
    sdk = []
    for i in range(1, 10):
        sdk += [i] * 9

    count = 0
    while True:
        shuffle(sdk)
        if validate_sudoku(sdk):
            return sdk
        count += 1
        print("attempt %s..." % count, end='\r')
