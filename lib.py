#!/usr/bin/python3

import operator
from heapq import heappush, heappushpop

def maxproduct(xs, ys, *, n, fn=operator.mul):
    t = []
    for x in sorted(xs, reverse=True):
        for y in sorted(ys, reverse=True):
            xy = fn(x, y)
            if len(t) < n:
                heappush(t, xy)
            else:
                if xy > t[0]:
                    heappushpop(t, xy)
                else:
                    break
    return sorted(t)

# vim:ts=4 sw=4 et
