import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
print(len(set(lst)))