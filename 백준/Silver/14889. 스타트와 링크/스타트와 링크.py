import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0 for _ in range(N)]
INF = 214412000000
res = INF
# L : 깊이, 
def dfs(L, idx):
    global res
    if L == N // 2:
        A = 0 # 스타트팀 점수
        B = 0 # 링크팀 점수
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += arr[i][j]
                elif not visited[i] and not visited[j]:
                    B += arr[i][j]
        res = min(res, abs(A-B))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(L+1, i+1)
            visited[i] = False
dfs(0, 0)
print(res)