import sys
input = sys.stdin.readline
A, B = map(int, input().split())
if A < B:
    print(B-A-1)
    for i in range(A+1, B):
        if i == B-1:
            print(i, end='')
        else:
            print(i, end=' ')
elif A > B:
    print(A - B - 1)
    for i in range(B + 1, A):
        if i == A - 1:
            print(i, end='')
        else:
            print(i, end=' ')
else:
    print(0)