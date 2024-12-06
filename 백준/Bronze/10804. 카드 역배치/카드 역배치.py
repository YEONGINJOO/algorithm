import sys
input = sys.stdin.readline
lst = [i for i in range(1, 21)]
for _ in range(10):
    a, b = map(int, input().split())
    temp = lst[a-1:b][::-1]
    fst = lst[:a-1]
    lat = lst[b:]
    lst = fst + temp + lat
print(*lst)