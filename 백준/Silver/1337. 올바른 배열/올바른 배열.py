import sys
input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
mn = 100
for i in range(n):
    cnt = 0
    arr = [0] * 5
    for j in range(5):
        arr[j] += lst[i] + j
        if arr[j] not in lst:
            cnt += 1
    if cnt < mn:
        mn = cnt
print(mn)