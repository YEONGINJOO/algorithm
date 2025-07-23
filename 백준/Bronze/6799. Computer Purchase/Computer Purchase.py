n = int(input())
lst = []
for _ in range(n):
    a = input().split()
    b = 2 * int(a[1]) + 3 * int(a[2]) + int(a[3])
    lst.append([a[0], b])
lst.sort(key = lambda x:(-x[1], x[0]))
if len(lst) == 1:
    print(lst[0][0])
elif len(lst) == 0:
    pass
else:
    print(lst[0][0])
    print(lst[1][0])