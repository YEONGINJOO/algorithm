import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
arr = {}
for _ in range(n):
    a, b = map(int, input().split())
    if a not in arr:
        arr[a] = b
    else:
        if arr[a] != b:
            cnt += 1
            arr[a] = b
print(cnt)