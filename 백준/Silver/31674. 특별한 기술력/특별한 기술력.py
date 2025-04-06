import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
MOD = 10 ** 9 + 7
a = lst[0]
a_sum = lst[0]
for i in range(1, N):
    a = lst[i] + a_sum
    a_sum += a
print(a_sum % MOD)