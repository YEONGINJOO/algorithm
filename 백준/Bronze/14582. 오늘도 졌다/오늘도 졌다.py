import sys
input = sys.stdin.readline
A = list(map(int, input().split()))
B = list(map(int, input().split()))

flag = 0
sma = 0
smb = 0
for i in range(9):
    sma += A[i]
    if sma > smb:
        flag = 1
    smb += B[i]
if flag:
    print('Yes')
else:
    print('No')