import sys
input = sys.stdin.readline
lst = list(map(int, input().split()))
a = sorted(lst)
while lst != a:
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i+1], lst[i] = lst[i], lst[i+1]
            print(*lst)