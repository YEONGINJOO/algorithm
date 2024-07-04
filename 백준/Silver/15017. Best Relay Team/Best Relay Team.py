import sys
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    a, b, c = map(str, input().split())
    lst.append([a, float(b), float(c)])
lst1 = sorted(lst, key=lambda x:x[1])
lst2 = sorted(lst, key=lambda x:x[2])
mn = 987654321
ans = []
for i in range(n):
    cnt = lst1[i][1]
    j = 0
    k = 0
    arr = [lst1[i][0]]
    while k < 3:
        if lst1[i][0] != lst2[j][0]:
            cnt += lst2[j][2]
            arr.append(lst2[j][0])
            k += 1
        j += 1
    if cnt < mn:
        mn = cnt
        ans = arr
print(mn)
for i in range(4):
    print(ans[i])