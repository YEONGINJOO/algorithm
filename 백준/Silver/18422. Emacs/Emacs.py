def count_rectangles(N, M, grid):
    visited = [[False] * M for _ in range(N)]
    rectangle_count = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == '*' and not visited[i][j]:
                # 새로운 직사각형 발견
                rectangle_count += 1
                
                # 직사각형의 경계를 찾기
                x_end, y_end = i, j
                
                # 오른쪽 경계 찾기
                while y_end < M and grid[i][y_end] == '*':
                    y_end += 1
                
                # 아래쪽 경계 찾기
                while x_end < N and all(grid[x_end][y] == '*' for y in range(j, y_end)):
                    x_end += 1
                
                # 방문 처리
                for x in range(i, x_end):
                    for y in range(j, y_end):
                        visited[x][y] = True

    return rectangle_count

N, M = map(int, input().strip().split())
grid = [input().strip() for _ in range(N)]

# 직사각형 개수 세기
result = count_rectangles(N, M, grid)
print(result)