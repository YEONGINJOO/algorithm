a = input()
if len(set(a)) == 1:
    print(0)
else:
    ans = ''
    for i in range(len(a)):
        if ans == '':
            ans += a[i]
        elif ans != '' and a[i-1] != a[i]:
            ans += a[i]
    cnt_0 = ans.count('0')
    cnt_1 = ans.count('1')
    if cnt_0 <= cnt_1:
        print(cnt_0)
    else:
        print(cnt_1)