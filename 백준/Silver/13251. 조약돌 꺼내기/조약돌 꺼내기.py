import sys
input = sys.stdin.readline
import math

m = int(input())
lst = list(map(int, input().split()))
k = int(input())
sm = sum(lst)
a = math.comb(sm, k)
b = 0
for i in range(m):
    if lst[i] < k:
        continue
    else:
        b += math.comb(lst[i], k)
print(b/a)