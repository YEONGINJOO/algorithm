import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b = map(str, input().strip().split())
    ans = int(a, 2) + int(b, 2)
    print(bin(ans)[2:])