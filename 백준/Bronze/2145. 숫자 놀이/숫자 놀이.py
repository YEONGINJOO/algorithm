while True:
    a = int(input())
    if a == 0:
        break
    while len(str(a)) > 1:
        cnt = 0
        for i in str(a):
            cnt += int(i)
        a = cnt
    print(a)