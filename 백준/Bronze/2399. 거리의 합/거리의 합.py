import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(map(int, input().split()))  # 리스트를 정렬
dist_sum = 0

for i in range(n):
    dist_sum += lst[i] * i - lst[i] * (n - i - 1)

print(dist_sum*2)