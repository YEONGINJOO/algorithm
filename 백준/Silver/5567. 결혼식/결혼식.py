from collections import deque

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(start):
    visited = [False] * (n+1)
    q = deque([start])
    visited[start] = True
    cnt = 0
    depth = 0
    while q and depth < 2:
        for _ in range(len(q)):
            current = q.popleft()
            for neighbor in arr[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
                    cnt += 1
        depth += 1
    return cnt
print(bfs(1))