import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
fruits = list(map(int, input().split()))

# 두 포인터와 과일 종류 카운트를 위한 딕셔너리
left = 0
max_length = 0
fruit_count = defaultdict(int)

for right in range(n):
    fruit_count[fruits[right]] += 1

    # 과일 종류가 2개를 초과하면 left 포인터를 이동
    while len(fruit_count) > 2:
        fruit_count[fruits[left]] -= 1
        if fruit_count[fruits[left]] == 0:
            del fruit_count[fruits[left]]
        left += 1

    # 현재 구간의 길이를 최대 길이와 비교
    max_length = max(max_length, right - left + 1)

print(max_length)