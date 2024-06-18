import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    s = 0
    cnt = 0
    for i in range(n):
        while True:
            if s == m or A[i] <= B[s]:
                cnt += s
                break
            else:
                s += 1
    print(cnt)