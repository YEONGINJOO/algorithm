import sys
input = sys.stdin.readline
n, m = map(int, input().split())
if n == 0:
    print(0)
else:
    lst = list(map(int, input().split()))
    sm = 0
    cnt = 0
    for i in range(n):
        if sm + lst[i] > m:
            sm = lst[i]
            cnt += 1
        else:
            sm += lst[i]
    if sm > 0:
        cnt += 1
    print(cnt)