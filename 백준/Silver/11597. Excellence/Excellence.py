import sys
input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
arr = []
for i in range(n//2):
    a = lst[i] + lst[-i-1]
    arr.append(a)
print(min(arr))
