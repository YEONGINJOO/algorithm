import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
lst = [[0] * n for _ in range(n)]
for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            if arr[j][i] == arr[k][i]:
                lst[k][j] = 1
                lst[j][k] = 1
cnt = []
for j in lst:
    cnt.append(j.count(1))
print(cnt.index(max(cnt))+1)