import sys
input = sys.stdin.readline
while True:
    d, m, y = map(int, input().split())
    yoon = 0
    cnt = 0
    if d == 0 and m == 0 and y == 0:
        break
    if y % 4 == 0 and y % 100 != 0:
        yoon = 1
    if y % 400 == 0:
        yoon = 1
    for i in range(1, m+1):
        if i == 2 and yoon == 1:
            cnt += 29
        elif i == 2 and yoon == 0:
            cnt += 28
        elif i == 4 or i == 6 or i == 9 or i == 11:
            cnt += 30
        else:
            cnt += 31
    if m == 2  and yoon == 1:
        d = 29 - d
    elif m == 2  and yoon == 0:
        d = 28 - d
    elif m == 4 or m == 6 or m == 9 or m == 11:
        d = 30 - d
    else:
        d = 31 - d
    cnt -= d
    print(cnt)