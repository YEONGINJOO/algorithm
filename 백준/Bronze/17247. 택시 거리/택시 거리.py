import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
temp = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            temp.append([i, j])
ans = abs(temp[0][0] - temp[1][0]) + abs(temp[0][1] - temp[1][1])
print(ans)