import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
arr = []
for i in range(n):
    if lst[i] == 0:
        arr.append(i + 1)
    else:
        arr.insert(len(arr)-lst[i],i+1)
print(*arr)