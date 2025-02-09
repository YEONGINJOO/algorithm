import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]
arr2 = [input().strip() for _ in range(N)]
flag = 1
temp = ''
for i in range(N):
    for j in range(M):
        temp += arr[i][j]
        temp += arr[i][j]
    arr[i] = temp
    temp = ''
for i in range(N):
    if arr[i] != arr2[i]:
        flag = 0
if flag:
    print('Eyfa')
else:
    print('Not Eyfa')