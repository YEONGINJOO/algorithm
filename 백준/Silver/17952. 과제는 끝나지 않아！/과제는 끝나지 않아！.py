import sys
input = sys.stdin.readline
n = int(input())
arr = []
cnt = 0
for _ in range(n):
    lst = list(map(int, input().split()))
    if lst[0] != 0:
        if lst[2]-1:
            arr.append([lst[1], lst[2]-1])
        else:
            cnt += lst[1]
    if arr != [] and lst[0] == 0:
        arr[-1][1] -= 1
        if arr[-1][1] == 0:
            cnt += arr[-1][0]
            arr.pop()
print(cnt)