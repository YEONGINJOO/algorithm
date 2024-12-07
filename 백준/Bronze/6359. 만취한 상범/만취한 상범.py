import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [1] * (n + 1)
    arr[0] = 0
    for i in range(2, n+1):
        for j in range(i, n+1, i):
            if arr[j] == 0:
                arr[j] = 1
            else:
                arr[j] = 0
    print(arr.count(1))