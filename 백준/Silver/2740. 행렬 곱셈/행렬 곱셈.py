import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr_1 = [list(map(int, input().split())) for _ in range(n)]
_, k = map(int, input().split())
arr_2 = [list(map(int, input().split())) for _ in range(m)]
lst = [[0]*k for _ in range(n)]
for row in range(n):
    for col in range(k):
        sm = 0
        for i in range(m):
            sm += arr_1[row][i] * arr_2[i][col]
        lst[row][col] = sm
for j in lst:
    print(*j)