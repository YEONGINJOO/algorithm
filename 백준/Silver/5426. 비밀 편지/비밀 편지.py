import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a = input().strip()
    n = int(len(a) ** (1/2))
    arr = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp += a[j+i*n]
        arr.append(temp[::-1])
    for i in range(n):
        for j in range(n):
            print(arr[j][i], end='')
    print()