import sys
input = sys.stdin.readline
import math
d, h, w = map(int, input().split())
r = (d ** 2 / (h ** 2 + w ** 2)) ** (1/2)
print(math.trunc(h*r), math.trunc(r*w))