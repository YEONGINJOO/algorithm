while True:
    n = int(input())
    if n == 0:
        break
    lst = []
    arr = []
    for i in range(n):
        a = input()
        lst.append(a)
        arr.append([a.lower(),i])
    arr.sort()
    print(lst[arr[0][1]])