import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
q = int(input())
for _ in range(q):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        a = arr[lst[1]-1].pop()
        arr[lst[1]-1].insert(0, a)
    else:
        A = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                A[j][n-i-1] = arr[i][j]
        arr = A
for i in range(n):
    print(*arr[i])