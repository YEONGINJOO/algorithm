import math
N = int(input())
# 열려 있는 창문의 개수는 N 이하의 최대 완전 제곱수 개수
result = int(math.isqrt(N))
print(result)