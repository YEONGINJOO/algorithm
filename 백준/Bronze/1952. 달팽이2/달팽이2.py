m, n = map(int, input().split())
arr = [[0] * n for _ in range(m)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
arr[0][0] = 1
i, j, dr = 0, 0, 0
cnt = 2
ans = 0
while cnt <= m * n:
    nx = i + delta[dr][0]
    ny = j + delta[dr][1]
    if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
        i, j = nx, ny
        arr[i][j] = cnt
        cnt += 1
    else:
        dr = (dr+1) % 4
        ans += 1
print(ans)