import sys
input = sys.stdin.readline

a, b = map(str, input().split())
str_a = list(map(int, a))
str_b = list(map(int, b))
print(sum(str_a) * sum(str_b))