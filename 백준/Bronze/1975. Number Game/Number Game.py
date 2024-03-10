import sys

# 재귀 함수를 사용하여 x를 b로 나누어 떨어지는 횟수를 계산합니다.
def calculate_zeros(x, b):
    if x % b == 0:
        return 1 + calculate_zeros(x // b, b)
    else:
        return 0

# 각 숫자에 대한 연속된 0의 합을 미리 계산하여 저장합니다.
precalculated_zeros = [0] * 1001
for num in range(2, 1001):
    precalculated_zeros[num] = sum(calculate_zeros(num, base) for base in range(2, num + 1))

# 입력된 테스트 케이스를 처리합니다.
input = sys.stdin.readline
num_of_cases = int(input())
for _ in range(num_of_cases):
    x = int(input())
    print(precalculated_zeros[x])