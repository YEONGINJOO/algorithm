from collections import defaultdict
import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
x_count = defaultdict(int)
y_count = defaultdict(int)

# 좌표 입력 받기
for _ in range(n):
    x, y = map(int, input().split())
    x_count[x] += 1
    y_count[y] += 1

# 평행한 직선 개수 세기
result = 0

# x좌표 기준으로 평행한 직선 개수 세기
for count in x_count.values():
    if count > 1:
        result += 1

# y좌표 기준으로 평행한 직선 개수 세기
for count in y_count.values():
    if count > 1:
        result += 1

# 결과 출력
print(result)