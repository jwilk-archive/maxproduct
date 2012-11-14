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

if __name__ == '__main__':
    from pprint import pprint
    pprint(maxproduct(range(1000), range(1000), n=10000))

# vim:ts=4 sw=4 et
