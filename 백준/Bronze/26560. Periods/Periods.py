import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a = sys.stdin.readline().strip()
    if a[-1] != '.':
        print(a+'.')
    else:
        print(a)