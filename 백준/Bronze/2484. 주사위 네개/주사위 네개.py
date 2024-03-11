import sys
input = sys.stdin.readline

N = int(input())
arr = [sorted(list(map(int, input().split()))) for _ in range(N)]
lst = []
mx = 0
for i in range(N):
    cnt = 0
    if len(set(arr[i])) == 1:
        cnt = 50000 + arr[i][0] * 5000
    elif len(set(arr[i])) == 2:
        if arr[i][1] == arr[i][2]:
            cnt = 10000 + arr[i][1] * 1000
        elif arr[i][1] != arr[i][2]:
            cnt = 2000 + arr[i][0] * 500 + arr[i][2] * 500
    elif len(set(arr[i])) == 3:
        if arr[i][0] == arr[i][1]:
            cnt = 1000 + arr[i][0] * 100
        elif arr[i][0] == arr[i][2]:
            cnt = 1000 + arr[i][0] * 100
        elif arr[i][0] == arr[i][3]:
            cnt = 1000 + arr[i][0] * 100
        elif arr[i][1] == arr[i][2]:
            cnt = 1000 + arr[i][1] * 100
        elif arr[i][2] == arr[i][3]:
            cnt = 1000 + arr[i][2] * 100
    else:
        cnt = max(arr[i]) * 100
    if cnt > mx:
        mx = cnt
print(mx)