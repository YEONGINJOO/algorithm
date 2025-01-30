import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    y, m = map(int, input().split())
    a = b = c = 0
    yoon = 0
    if y % 100 != 0 and y % 4 == 0 or y % 400 == 0:
        yoon = 1
    if yoon:
        if m == 3:
            b = 2
            c = 29
            a = y
        else:
            if m == 1:
                a = y-1
                b = 12
                c = 31
            elif m == 2 or m == 4 or m == 6 or m == 8 or m == 9 or m == 11:
                a = y
                b = m-1
                c = 31
            elif m == 5 or m == 7 or m == 10 or m == 12:
                a = y
                b = m - 1
                c = 30
    else:
        if m == 1:
            a = y-1
            b = 12
            c = 31
        elif m == 3:
            a = y
            b = 2
            c = 28
        elif m == 2 or m == 4 or m == 6 or m == 8 or m == 9 or m == 11:
            a = y
            b = m-1
            c = 31
        elif m == 5 or m == 7 or m == 10 or m == 12:
            a = y
            b = m - 1
            c = 30
    print(a, b, c)