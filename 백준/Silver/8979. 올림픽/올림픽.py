import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = sorted(arr, key=lambda x: (x[1], x[2], x[3]), reverse=True)
ans = 0
for i in range(n):
    if arr[i][0] == k:
        if arr[i] == arr[i-1]:
            ans = i
        else:
            ans = i + 1
        break
print(ans)