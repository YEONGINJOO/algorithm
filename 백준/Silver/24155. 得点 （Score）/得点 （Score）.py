import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
a = sorted(lst, reverse=True)
rank = [a.index(i) + 1 for i in lst]
for j in rank:
    print(j)