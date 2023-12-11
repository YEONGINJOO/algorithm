while True:
    a, b = map(str, input().split())
    if a == '0' and b == '0':
        break
    st_size = max(len(a), len(b)) - min(len(a), len(b))
    if len(a) > len(b):
        b = st_size * '0' + b
    if len(b) > len(a):
        a = st_size * '0' + a
    cnt = 0
    carry = 0
    for i in range(len(a)-1, -1, -1):
        if int(a[i]) + int(b[i]) + carry >= 10:
            cnt += 1
            carry = 1
        else:
            carry = 0
    print(cnt)