import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = {}
cnt = 0
for i in range(n):
    s, y = map(int, input().split())
    if (s, y) in arr:
        arr[(s, y)] += 1
    else:
        arr[(s,y)] = 1
for i in arr:
    if arr[i] <= k:
        cnt += 1
    else:
        if arr[i] % k == 0:
            cnt += arr[i] // k
        else:
            cnt += arr[i] // k + 1
print(cnt)