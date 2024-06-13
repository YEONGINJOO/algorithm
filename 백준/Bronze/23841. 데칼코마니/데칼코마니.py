import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] != '.':
            arr[i][-j-1] = arr[i][j]
for k in range(n):
    if k != 0:
        print()
    for l in range(m):
        print(arr[k][l], end='')