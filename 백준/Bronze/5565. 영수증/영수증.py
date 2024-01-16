import sys
input = sys.stdin.readline
n = int(input())
ans = 0
for _ in range(9):
    a = int(input())
    ans += a
print(n-ans)