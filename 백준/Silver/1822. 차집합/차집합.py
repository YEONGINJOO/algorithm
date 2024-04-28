import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
lst = list(A-B)
if lst == []:
    print(0)
else:
    lst.sort()
    print(len(lst))
    print(*lst)