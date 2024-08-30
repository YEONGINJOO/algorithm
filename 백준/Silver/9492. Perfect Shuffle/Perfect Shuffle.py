import sys
input = sys.stdin.readline

while True:
    t = int(input())
    if t == 0:
        break
    lst = [input().strip() for _ in range(t)]
    arr = []
    if t % 2 == 0:
        a = lst[:t//2]
        b = lst[t//2:]
    else:
        a = lst[:t//2+1]
        b = lst[t//2+1:]
    for i in range(len(b)):
        print(a[i])
        print(b[i])
    if t % 2 != 0:
        print(a[-1])