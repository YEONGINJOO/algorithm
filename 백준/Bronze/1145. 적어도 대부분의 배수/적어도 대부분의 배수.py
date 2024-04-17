import sys
input = sys.stdin.readline
lst = list(map(int, input().split()))
mn = min(lst)
while True:
    cnt = 0
    for i in lst:
        if mn % i == 0:
            cnt += 1
    if cnt >= 3:
        print(mn)
        break
    mn += 1