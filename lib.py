# Copyright © 2012-2017 Jakub Wilk <jwilk@jwilk.net>
# SPDX-License-Identifier: MIT

import operator
from heapq import heappush, heappushpop

def maxproduct(xs, ys, *, n, fn=operator.mul, reverse=False):
    t = []
    xs = sorted(xs, reverse=True)
    ys = sorted(ys, reverse=True)
    for x in xs:
        for y in ys:
            xy = fn(x, y)
            if len(t) < n:
                heappush(t, xy)
            else:
                if xy > t[0]:
                    heappushpop(t, xy)
                else:
                    break
    return sorted(t, reverse=reverse)

# vim:ts=4 sts=4 sw=4 et
