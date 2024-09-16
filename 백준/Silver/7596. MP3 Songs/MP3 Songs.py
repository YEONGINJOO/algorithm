import sys
input = sys.stdin.readline
j = 1
while True:
    n = int(input())
    if n == 0:
        break
    lst = [input().strip() for _ in range(n)]
    lst.sort()
    print(j)
    for i in range(n):
        print(lst[i])
    j += 1