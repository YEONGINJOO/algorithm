import sys
input = sys.stdin.readline
n = int(input())
sx = sy = 0
sx2 = sy2 = 0
sxy = 0
for _ in range(n):
    x, y = map(int, input().split())
    sx += x
    sy += y
    sx2 += x**2
    sy2 += y**2
    sxy += x * y
try:
    a = (n * sxy - sx * sy) / (n * sx2 - sx**2)
    b = (sy - a *sx) / n
    print(a, b)
except ZeroDivisionError:
    print('EZPZ')