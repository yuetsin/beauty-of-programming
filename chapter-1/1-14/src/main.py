#!/usr/bin/env python3
from game import Game

width = int(input("chessboard width? >>> "))
height = int(input("chessboard height? >>> "))
patterns = input("chessboard shape patterns? >>> ")

game = Game(width, height, patterns)


def convert_pos(row: str, col: str) -> (int, int):
    return int(col) - 1, ord(row) - ord('A')


while True:
    if game.is_game_over():
        print("congratulations! game clear!")
        break
    elif game.is_dead_lock():
        print("here's a deadlock...")
    game.print_chess()
    command = input("""You can input the following instructions to play:
    1. LINK <Row> <Column> <Row> <Column>
        for example, LINK A 5 B 11
    2. SHUFFLE
        to refresh the table pattern
>>> """).strip()

    tokens = [tok.upper() for tok in command.split(' ')]
    if len(tokens) < 1:
        print("invalid command.")
    elif tokens[0] == 'LINK':
        if len(tokens) != 5:
            print("invalid command %s." % ' + '.join(tokens))
            continue
        since = convert_pos(tokens[1], tokens[2])
        till = convert_pos(tokens[3], tokens[4])
        if game.try_link(since, till):
            print("successfully linked-up %s%s and %s%s." %
                  (tokens[1], tokens[2], tokens[3], tokens[4]))
        else:
            print("failed to link-up %s%s and %s%s." %
                  (tokens[1], tokens[2], tokens[3], tokens[4]))
    elif tokens[0] == 'SHUFFLE':
        if len(tokens) != 1:
            print("invalid command %s." % ' + '.join(tokens))
            continue
        game.shuffle()
