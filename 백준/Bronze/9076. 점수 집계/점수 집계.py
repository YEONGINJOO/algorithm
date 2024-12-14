import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    lst = list(map(int, input().split()))
    lst.sort()
    a = lst[1:-1]
    if a[-1] - a[0] >= 4:
        print('KIN')
    else:
        print(sum(a))