import sys
input = sys.stdin.readline

n = int(input())
lst = [input().strip() for _ in range(n)]
for i in range(n):
    if lst[i][::-1] in lst:
        print(len(lst[i]), lst[i][len(lst[i])//2])
        break