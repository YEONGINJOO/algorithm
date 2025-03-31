import sys
input = sys.stdin.readline
from collections import deque
delta = [(0, 1), (1, 0)]

def bfs(x, y, arr):
    q = deque()
    q.append([x, y])

    visited = [[False] * n for _ in range(m)]
    visited[x][y] = True

    while q:
        a, b = q.popleft()
        if a == m - 1 and b == n - 1:
            return True

        for di, dj in delta:
            ni = a + di
            nj = b + dj
            if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))
    return False

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
a = bfs(0, 0, arr)
print("Yes" if bfs(0, 0, arr) else "No")