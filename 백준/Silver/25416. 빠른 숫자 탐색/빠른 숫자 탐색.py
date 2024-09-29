from collections import deque

arr = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

# 이동 방향 설정 (우, 좌, 하, 상)
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(start_r, start_c):
    queue = deque([(start_r, start_c, 0)]) # (행, 열, 이동 횟수)
    visited = [[False] * 5 for _ in range(5)]
    visited[start_r][start_c] = True

    while queue:
        x, y, steps = queue.popleft()
        
        # 1이 있는 칸을 찾으면 이동 횟수 반환
        if arr[x][y] == 1:
            return steps
        
        # 네 방향으로 이동
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            
            # 이동 가능한 범위 체크
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and arr[nx][ny] != -1:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))
    
    return -1  # 1에 도달할 수 없는 경우

# BFS 호출
result = bfs(r, c)
print(result)