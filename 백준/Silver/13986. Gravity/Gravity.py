import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
for i in range(m):
    for _ in range(n):
        for j in range(1, n, 1):
            # print(arr[-j][i])
            if arr[-j][i] == '.' and arr[-j-1][i] == 'o':
                arr[-j][i] = 'o'
                arr[-j-1][i] = '.'
            elif arr[-j][i] == '#' and arr[-j-1][i] == 'o':
                continue
for i in range(n):
    for j in range(m):
        print(arr[i][j], end='')
    print()