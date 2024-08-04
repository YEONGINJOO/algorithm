import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a = input().strip().split()
    for i in range(len(a)):
        print(a[i][::-1], end=' ')