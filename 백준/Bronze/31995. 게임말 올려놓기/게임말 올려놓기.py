N = int(input())
M = int(input())
arr = [[0] * N for _ in range(M)]
if N == 1 or M == 1:
    print(0)
else:
    print((2*N-2) * (M-1))