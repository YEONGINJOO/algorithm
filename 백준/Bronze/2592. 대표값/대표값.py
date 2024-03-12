import sys
input = sys.stdin.readline

lst = [int(input()) for _ in range(10)]
lst.sort()
av = sum(lst) / 10
mx = 0
mod = 0
for i in range(10):
    cnt = 0
    for j in range(10):
        if lst[i] == lst[j]:
            cnt += 1
    if cnt > mx:
        mx = cnt
        mod = lst[i]
print(int(av))
print(mod)