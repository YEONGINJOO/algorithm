import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
cnt = 0

for i in range(n):
    flag = 0
    for j in range(m):
        if arr[i][j] == 'X':
            flag = 1
    if flag == 0:
        for k in range(m):
            ktatus = 0
            for l in range(n):
                if arr[l][k] == 'X':
                    ktatus = 1
            if ktatus == 0:
                arr[i][k] = 'X'
                break
        cnt += 1
for i in range(m):
    status = 0
    for j in range(n):
        if arr[j][i] == 'X':
            status = 1
    if status == 0:
        cnt += 1
print(cnt)