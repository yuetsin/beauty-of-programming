#!/usr/bin/env python

from exceptions import NoSolutionException, InfiniteSolutionException


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

    def __repr__(self):
        return "<Light: a = %.4f, b = %.4f, c = %.4f>" % (self.a, self.b, self.c)

    def intersect(self, light) -> tuple:
        if self.a == light.a and self.b == light.b:
            if self.c == light.c:
                raise InfiniteSolutionException
            else:
                raise NoSolutionException

        x = (light.b*self.c + self.b*light.c) / \
            (-light.a*self.b + self.a*light.b)

        y = (light.a*self.c + self.a*light.c) / \
            (light.a*self.b - self.a*light.b)

        return (x, y)
