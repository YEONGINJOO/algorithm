import sys
import math
input = sys.stdin.readline

n, d, p = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if a[i] > 0:
        while a[i] > 0:
            a[i] -= d
            cnt += 1
        if i < n-1:
            j = math.floor(abs(a[i]) * p / 100)
            a[i+1] -= j
print(cnt)
