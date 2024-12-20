import sys
input = sys.stdin.readline
while True:
    h = int(input())
    if h == 0:
        break
    mx = h
    while h > 1:
        if h % 2 == 0:
            h = h // 2
        else:
            h = h * 3 + 1
        if h > mx:
            mx = h
    print(mx)