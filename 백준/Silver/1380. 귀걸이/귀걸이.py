import sys
input = sys.stdin.readline
j = 1
while True:
    n = int(input())
    if n == 0:
        break
    lst = [sys.stdin.readline().strip() for _ in range(n)]
    arr = []
    for i in range(2*n-1):
        a, b = map(str, sys.stdin.readline().strip().split())
        if int(a) not in arr:
            arr.append(int(a))
        else:
            arr.remove(int(a))
    print(j, lst[arr[0]-1])
    j += 1