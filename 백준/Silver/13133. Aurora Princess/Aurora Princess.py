import sys
input = sys.stdin.readline
n = int(input())
arr = []
cnt = 0
for i in range(1, n+1):
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        flag = 0
    else:
        flag = 1
    arr.append([a, b, i, flag])
m = int(input())
lst = list(map(int, input().split()))
for j in range(n):
    if arr[j][2] in lst:
        arr[j][3] = 0
    if arr[j][3] != 0:
        if arr[j][0] not in lst and arr[j][1] not in lst:
            cnt += 1
print(cnt)