a = int(input())
if a < 10:
    a_st = '0' + str(a)
else:
    a_st = str(a)
cnt = 0
if a == 0:
    cnt = 1
else:
    while True:
        b = int(a_st[0]) + int(a_st[1])
        if len(str(b)) > 1:
            a_st = a_st[1] + str(b)[1]
        else:
            a_st = a_st[1] + str(b)
        cnt += 1
        if int(a_st) == a:
            break
print(cnt)