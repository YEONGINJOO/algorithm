import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
lst = [0] * 101
mn = 101
mx = 0
sm = 0
for _ in range(3):
    ar, de = map(int, input().split())
    for i in range(ar, de):
        lst[i] += 1
    if ar < mn:
        mn = ar
    if de > mx:
        mx = de
for i in range(mn, mx):
    if lst[i] == 1:
        sm += a
    elif lst[i] == 2:
        sm += b * 2
    elif lst[i] == 3:
        sm += c * 3
print(sm)