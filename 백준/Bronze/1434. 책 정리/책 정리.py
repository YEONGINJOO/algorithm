import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
lst = []
for i in range(n):
    for j in range(m):
        if A[i] >= B[j]:
            A[i] -= B[j]
            B[j] = 0
print(sum(A))