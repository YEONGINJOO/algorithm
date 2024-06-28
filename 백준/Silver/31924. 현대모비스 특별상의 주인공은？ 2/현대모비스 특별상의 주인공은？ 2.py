import sys
input = sys.stdin.readline

def count_mobis(grid, N):
    # "MOBIS" 문자열을 찾기 위해 필요한 방향 벡터 (8방향)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    target = "MOBIS"
    target_len = len(target)
    count = 0

    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < N

    def search(x, y, dx, dy):
        for i in range(target_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != target[i]:
                return False
        return True

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'M':
                for dx, dy in directions:
                    if search(i, j, dx, dy):
                        count += 1

    return count

N = int(input())
grid = [input().strip() for _ in range(N)]

print(count_mobis(grid, N))