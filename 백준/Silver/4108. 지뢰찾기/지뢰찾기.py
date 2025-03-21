import sys
input = sys.stdin.readline
while True:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break
    arr = [list(input().strip()) for _ in range(r)]
    delta = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for i in range(r):
        for j in range(c):
            cnt = 0
            if arr[i][j] == '*':
                continue
            else:
                for di, dj in delta:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < r and 0 <= nj < c:
                        if arr[ni][nj] == '*':
                            cnt += 1
                arr[i][j] = cnt
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end='')
        print()