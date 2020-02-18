#!/usr/bin/env python


class Drink:

    name = ""
    volume = 0
    max_amount = 0
    satisfactoriness = 0

    def __init__(self, name: str, volume: int, max_amount: int, satisfactoriness: int):
        self.name = name
        self.volume = volume
        self.max_amount = max_amount
        self.satisfactoriness = satisfactoriness

    def __str__(self):
        return "Drink(name=%s, volume=%d, max_amount=%d, satisfactoriness=%d)" % (self.name, self.volume, self.max_amount, self.satisfactoriness)
