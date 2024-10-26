import sys
input = sys.stdin.readline

def cnt(r, c):
    MOD = 998244353
    if c == 1:
        return r % MOD
    if r == 1:
        return 0
    ways = r * pow(r-1, c-1, MOD) % MOD
    return ways

r, c = map(int, input().split())
print(cnt(r, c))