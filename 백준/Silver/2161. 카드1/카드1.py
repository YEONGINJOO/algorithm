N = int(input())
lst = [i for i in range(1, N+1)]
a_lst = []
while len(lst) > 0:
    a_lst.append(lst.pop(0))
    if lst:
        lst.append(lst.pop(0))
print(*a_lst)