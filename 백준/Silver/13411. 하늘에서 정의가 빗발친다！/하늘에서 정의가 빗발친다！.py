import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    x, y, v = map(int, input().split())
    a = (x ** 2 + y ** 2) ** (1/2)
    a = a / v
    lst.append([a, i+1])
lst.sort()
for i in range(n):
    print(lst[i][1])