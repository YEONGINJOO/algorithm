for _ in range(3):
    a = input()
    cnt = 1
    lst = []
    for i in range(7):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            lst.append(cnt)
            cnt = 1
    lst.append(cnt)
    print(max(lst))