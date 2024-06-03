import sys
input = sys.stdin.readline

n = int(input())
lst = []
mx = 0
mxidx = 0
for i in range(n):
    cnt = 2
    a = n - i
    lst.append([n,a])
    while True:
        if lst[i][-2] - lst[i][-1] < 0:
            break
        else:
            lst[i].append(lst[i][-2] - lst[i][-1])
            cnt += 1
    if cnt > mx:
        mx = cnt
        mxidx = i
print(mx)
print(*lst[mxidx])