import sys
input = sys.stdin.readline

n = int(input())
a = "SciComLove"
for i in range(n):
    a = a[::-1]
print(a)