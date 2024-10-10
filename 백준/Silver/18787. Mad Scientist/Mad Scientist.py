import sys
input = sys.stdin.readline
N = int(input())
A = input().strip()
B = input().strip()
cnt = 0
i= 0
while i < N:
    if A[i] != B[i]:
        for j in range(i+1, N):
            if A[j] == B[j]:
                i = j
                break
        cnt += 1
    i += 1
print(cnt)