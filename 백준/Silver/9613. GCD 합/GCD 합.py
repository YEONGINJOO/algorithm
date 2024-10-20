import math
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, *lst = map(int, input().split())
    sm = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sm += math.gcd(lst[i], lst[j])
    print(sm)