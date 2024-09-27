import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key = lambda x:(x[0], -x[1]))
sm = 0
for i in range(n):
    sm += lst[i][0] * (i+1) + lst[i][1]
print(sm)