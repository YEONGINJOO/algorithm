while True:
    a = input()
    if a == '#':
        break
    a = a.lower()
    lst = a.split()
    cnt = 0
    for i in range(1, len(lst)):
        for j in lst[i]:
            if j == lst[0]:
                cnt += 1
    print(lst[0], cnt)