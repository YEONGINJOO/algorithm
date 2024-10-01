import sys
input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse = True)
for i in range(n):
    print(lst[i])