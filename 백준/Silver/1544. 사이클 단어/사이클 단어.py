import sys
input = sys.stdin.readline
n = int(input())
lst = [input().strip() for _ in range(n)]
cnt = 0
for i in range(n):
    a = lst[i]
    for j in range(len(lst[i])):
        a = a[1:] + a[0]
        if a in lst:
            lst[i] = a
set_lst = set(lst)
print(len(set_lst))