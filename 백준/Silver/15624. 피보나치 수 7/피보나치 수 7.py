import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
    sys.exit()
elif n == 1:
    print(1)
    sys.exit()

MOD = 1000000007
a, b = 0, 1

for _ in range(2, n + 1):
    a, b = b, (a + b) % MOD

print(b)