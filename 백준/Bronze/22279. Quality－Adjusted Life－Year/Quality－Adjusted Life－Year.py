import sys
input = sys.stdin.readline

n = int(input())
lst = [sys.stdin.readline().strip().split() for _ in range(n)]
ans = 0
for i in range(n):
    ans += float(lst[i][0]) * float(lst[i][1])
print(f'{ans:.3f}')