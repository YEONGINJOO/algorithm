import sys
input = sys.stdin.readline

def sol(s, lst):
    s0 = s
    U = 0
    for i in lst:
        if i == 1:
            if U == s0:
                s0 *= 2
            U += 1
        elif i == 0:
            U -= 1
    return s0

s, n, m = map(int, input().split())
lst = [int(input()) for _ in range(m+n)]
print(sol(s, lst))