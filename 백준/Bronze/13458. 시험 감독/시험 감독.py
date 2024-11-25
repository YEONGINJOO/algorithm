import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for i in range(N):
    temp = A[i] - B
    cnt += 1
    if temp <= 0:
        continue
    else:
        if temp < C:
            cnt += 1
        else:
            if temp % C == 0:
                cnt += temp // C
            else:
                cnt += temp // C + 1
print(cnt)