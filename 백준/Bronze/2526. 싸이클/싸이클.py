import sys
input = sys.stdin.readline

n, p = map(int, input().split())
lst = []
num = n
while True:
    num = (num * n) % p
    if num in lst:
        print(len(lst) - lst.index(num))
        break
    lst.append(num)