import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '*' and not visited[i][j]:
            cnt += 1
            x, y = i, j
            while y < M and arr[i][y] == '*':
                y += 1

            while x < N and all(arr[x][k] == '*' for k in range(j, y)):
                x += 1

            for n in range(i, x):
                for m in range(j, y):
                    visited[n][m] = True
print(cnt)