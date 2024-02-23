import sys
input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]
if lst[1] - lst[0] == lst[2] - lst[1]:
    ans = lst[-1] + lst[1] - lst[0]
elif lst[1] / lst[0] == lst[2] / lst[1]:
    ans = lst[-1] * (lst[1] / lst[0])
print(int(ans))