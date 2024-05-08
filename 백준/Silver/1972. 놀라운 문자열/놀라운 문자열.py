while True:
    a = input()
    if a == '*':
        break
    i = 1
    flag = 1
    while i < len(a):
        lst = []
        for j in range(len(a)-i):
            temp = ''
            temp += a[j]+a[j+i]
            lst.append(temp)
        set_lst = set(lst)
        if len(set_lst) == len(lst):
            flag = 1
        else:
            flag = 0
            break
        i += 1
    if flag == 0:
        print(f'{a} is NOT surprising.')
    else:
        print(f'{a} is surprising.')