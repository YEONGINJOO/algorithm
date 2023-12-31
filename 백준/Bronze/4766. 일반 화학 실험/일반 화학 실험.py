lst = []
while True:
    a = float(input())
    if a == 999:
        break
    lst.append(a)
    if len(lst) > 1:
        a = lst[1]-lst[0]
        print(f'{a:.2f}')
        lst.remove(lst[0])