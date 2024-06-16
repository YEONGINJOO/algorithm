import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a = sys.stdin.readline().strip()
    if 'S' in a:
        print(a)
        break