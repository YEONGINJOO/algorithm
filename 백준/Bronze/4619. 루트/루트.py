while True:
    b, n = map(int, input().split())
    if b == 0 and n == 0:
        break
    lst = []
    for i in range(1, b+1):
        a = i**n
        lst.append([abs(b-a),i])
        if len(lst) > 1 and lst[i-2][0] < lst[i-1][0]:
            break
    lst.sort()
    print(lst[0][1])