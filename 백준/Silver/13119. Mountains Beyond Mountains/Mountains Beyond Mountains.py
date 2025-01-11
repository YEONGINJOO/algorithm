import sys
input = sys.stdin.readline
N, M, X = map(int, input().split())
lst = list(map(int, input().split()))
arr = [['.'] * M for _ in range(N)]
for i in range(M):
    arr[X - 1][i] = '-'
    for j in range(lst[i]):
        if j == X-1:
            arr[j][i] = '*'
        else:
            arr[j][i] = '#'
    if (i + 1) % 3 == 0:
        for k in range(X-lst[i]-1):
            arr[k+lst[i]][i] = '|'
arr = arr[::-1]
for i in range(N):
    print(''.join(arr[i]))