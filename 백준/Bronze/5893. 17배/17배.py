import sys
input = sys.stdin.readline

n = int(input())
a = int(str(n), 2) * 17
ans = bin(a)
print(ans[2:])