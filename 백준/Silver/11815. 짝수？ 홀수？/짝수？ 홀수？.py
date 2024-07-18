import sys
import math

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
arr = []

for i in range(n):
    root = int(math.isqrt(x[i]))
    if root * root == x[i]:
        arr.append(1)
    else:
        arr.append(0)
print(*arr)