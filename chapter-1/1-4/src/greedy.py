#!/usr/bin/env python

# greedy: is that correct?

books = [2, 2, 2, 1, 1]

per_price = 8

discounts = {
    5: 0.25,
    4: 0.2,
    3: 0.1,
    2: 0.05,
    1: 0.0
}

cost = 0.0

while sum(books):
    diff_kinds = sum([1 if v else 0 for v in books])

    if diff_kinds == 1:
        cost += max(books) * per_price
        break

    cost += per_price * diff_kinds * (1 - discounts[diff_kinds])
    books = [v - 1 if v > 0 else 0 for v in books]

print("total price: %.2f" % cost)
