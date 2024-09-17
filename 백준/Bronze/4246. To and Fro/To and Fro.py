import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    a = input().strip()
    arr = []
    for i in range(len(a)//n):
        temp = []
        for j in range(i*n, i*n+n):
            temp.append(a[j])
        if i % 2 != 0:
            arr.append(temp[::-1])
        else:
            arr.append(temp)
    for i in range(n):
        for j in range(len(arr)):
            print(arr[j][i], end='')
    print()
