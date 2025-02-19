import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
A = list(map(int, input().split()))
cnt = [0] * N
for i in range(M):
    b = list(map(int, input().split()))
    for j in range(N):
        if b[j] == A[i]:
            cnt[j] += 1
        else:
            cnt[A[i]-1] += 1
for k in range(N):
    print(cnt[k])