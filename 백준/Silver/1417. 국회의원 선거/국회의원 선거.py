N = int(input())
lst = [int(input()) for _ in range(N)]
dasom = lst[0]
if len(lst) == 1:
    print(0)
else:
    a_lst = lst[1:]
    a_lst.sort(reverse = True)
    # print(a_lst)
    cnt = 0
    while dasom <= a_lst[0]:
        dasom += 1
        a_lst[0] -= 1
        cnt += 1
        a_lst.sort(reverse = True)
    print(cnt)