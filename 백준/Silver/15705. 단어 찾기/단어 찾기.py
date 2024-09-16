import sys
input = sys.stdin.readline

s = input().strip()
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
delta = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]

def exists_word(x, y, dx, dy):
    for k in range(len(s)):
        nx, ny = x + dx * k, y + dy * k
        if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != s[k]:
            return False
    return True

for i in range(n):
    for j in range(m):
        for dx, dy in delta:
            if exists_word(i, j, dx, dy):
                print(1)
                sys.exit(0)

print(0)