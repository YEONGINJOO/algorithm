while True:
    a, b, c, d, e, f = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
        break
    lst = [a,b,c,d,e,f]
    lst.sort()
    ans = lst[1]+lst[2]+lst[3]+lst[4]
    if ans % 4:
        print(ans/4)
    else:
        print(int(ans/4))