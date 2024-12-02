import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
arr = arr[::-1]
mx = arr[0]
cnt = 1
for i in range(1, N):
    if arr[i] > mx:
        cnt += 1
        mx = arr[i]
print(cnt)