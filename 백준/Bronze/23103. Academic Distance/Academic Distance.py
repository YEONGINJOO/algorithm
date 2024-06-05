import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
distance = 0
for i in range(n-1):
    distance += abs(lst[i][0] - lst[i+1][0]) + abs(lst[i][1] - lst[i+1][1])
print(distance)