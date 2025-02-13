import sys
input = sys.stdin.readline
k = 1
while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for _ in range(n):
        a = input().strip()
        b = len(a)
        arr.append([a, b])
    arr.sort(key = lambda x:x[1])
    a = []
    b = []
    for i in range(n):
        if i % 2 == 0:
            a.append(arr[i][0])
        else:
            b.append(arr[i][0])
    b = b[::-1]
    ans = a + b
    print(f'SET {k}')
    for j in ans:
        print(j)
    k += 1