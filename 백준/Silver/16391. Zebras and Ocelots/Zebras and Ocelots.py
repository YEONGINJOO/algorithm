import sys
input = sys.stdin.readline
n = int(input())
ans = 0
for _ in range(n):
    c = input().strip()
    ans = (ans << 1) | (1 if c == 'O' else 0)
print(ans)