import sys
input = sys.stdin.readline

l = int(input())
lst = list(map(int, input().split()))
n = int(input())
lst.sort()
if n in lst:
    print(0)
else:
    mn = 0
    mx = 0
    for i in lst:
        if i < n:
            mn = i
        elif i > n and mx == 0:
            mx = i
    print((n-mn)*(mx-n)-1)