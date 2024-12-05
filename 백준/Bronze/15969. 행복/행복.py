import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(lst[-1] - lst[0])