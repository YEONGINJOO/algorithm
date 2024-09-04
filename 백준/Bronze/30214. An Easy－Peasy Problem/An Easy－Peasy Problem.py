import sys
input = sys.stdin.readline
s1, s2 = map(int, input().split())
if s1 >= s2 / 2:
    print('E')
else:
    print('H')
