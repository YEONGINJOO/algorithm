import sys
input = sys.stdin.readline

while True:
    n, *lst = map(int, input().split())
    if n == 0:
        break
    arr = [lst[0]]
    for i in range(1, n):
        if lst[i-1] != lst[i]:
            arr.append(lst[i])
    print(*arr, end=' ')
    print('$')