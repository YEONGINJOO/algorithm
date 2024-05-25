import sys
input = sys.stdin.readline
n = int(input())
lst =[list(map(int, input().split())) for _ in range(n)]
ans = 0
mx = 0
for i in range(n):
    for j in range(3):
        for k in range(j+1, 4):
            sm = 0
            for h in range(k+1, 5):
                sm = lst[i][j] + lst[i][k] + lst[i][h]
                a = sm % 10
                if a >= mx:
                    mx = a
                    ans = i
print(ans+1)