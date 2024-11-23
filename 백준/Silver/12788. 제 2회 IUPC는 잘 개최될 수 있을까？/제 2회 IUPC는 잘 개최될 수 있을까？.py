import sys
input = sys.stdin.readline

n = int(input())
m, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
sm = m * k
temp = 0
cnt = 0
for i in range(n):
    temp += A[i]
    cnt += 1
    if temp >= sm:
        break
if temp >= sm:
    print(cnt)
else:
    print('STRESS')