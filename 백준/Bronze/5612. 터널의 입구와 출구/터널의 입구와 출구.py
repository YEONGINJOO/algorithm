import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = m
lst = [m]
for _ in range(n):
    a, b = map(int, input().split())
    s += a
    s -= b
    if s < 0:
        lst = []
        break
    else:
        lst.append(s)
if lst == []:
    print(0)
else:
    print(max(lst))