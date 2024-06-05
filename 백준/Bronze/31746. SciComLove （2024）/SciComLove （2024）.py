import sys
input = sys.stdin.readline

n = int(input())
a = "SciComLove"
if n % 2 == 0:
    print(a)
else:
    print(a[::-1])