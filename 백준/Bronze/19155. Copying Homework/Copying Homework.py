import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
a = max(lst)
ans = [a-i+1 for i in lst]
print(*ans)