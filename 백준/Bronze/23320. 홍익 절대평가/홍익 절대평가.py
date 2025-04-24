import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
x, y = map(int, input().split())
lst.sort()
a1 = n * x//100
a2 = 0
for i in range(n):
    if lst[i] >= y:
        a2 += 1
print(a1, a2)