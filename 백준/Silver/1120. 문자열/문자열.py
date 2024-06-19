import sys

a, b = map(str, sys.stdin.readline().strip().split())

if len(a) == len(b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)
else:
    mn = 123456789
    for i in range(len(b)-len(a)+1):
        cnt = 0
        for j in range(len(a)):
            if a[j] != b[i:i+len(a)][j]:
                cnt += 1
        if mn > cnt:
            mn = cnt
    print(mn)