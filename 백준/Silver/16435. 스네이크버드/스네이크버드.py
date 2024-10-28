import sys
input = sys.stdin.readline
n, h = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for i in range(n):
    if lst[i] <= h:
        h += 1
print(h)