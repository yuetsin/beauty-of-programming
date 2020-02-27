#!/usr/bin/env python


class Light:
    # 一般式：
    # a \times x + b \times y + c = 0
    a: float = 0.0
    b: float = 0.0
    c: float = 0.0

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
