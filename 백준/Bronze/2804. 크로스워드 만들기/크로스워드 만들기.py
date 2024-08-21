import sys
input = sys.stdin.readline
A, B = input().strip().split()
arr = [['.'] * len(A) for _ in range(len(B))]
Aidx = 0
Bidx = 0
same = ''
for i in range(len(A)):
    if A[i] in B:
        Aidx = i
        same = A[i]
        break
Bidx = B.index(same)
for i in range(len(B)):
    for j in range(len(A)):
        if i == Bidx and j < len(A):
            arr[i][j] = A[j]
        if j == Aidx and i < len(B):
            arr[i][j] = B[i]
        print(arr[i][j], end='')
    print()