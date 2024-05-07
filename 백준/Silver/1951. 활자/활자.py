import sys
input = sys.stdin.readline

n = int(input())
str_n = str(n)
cnt = 0
for i in range(1, len(str_n)+1):
    cnt += 9 * (10 ** (i-1)) * i
cnt = cnt - (int('9' * len(str_n)) - n) * len(str_n)
print(cnt % 1234567)