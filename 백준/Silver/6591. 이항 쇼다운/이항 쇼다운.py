import sys
input = sys.stdin.readline
import math
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    ans = math.comb(a, b)
    print(ans)