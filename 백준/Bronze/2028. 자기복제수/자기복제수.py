t = int(input())
for _ in range(t):
    n = int(input())
    a = n ** 2
    str_n = str(n)
    str_a = str(a)
    cnt = 0
    for i in range(1, len(str_n)+1):
        if str_a[-i] == str_n[-i]:
            cnt += 1
    if cnt == len(str_n):
        print('YES')
    else:
        print('NO')