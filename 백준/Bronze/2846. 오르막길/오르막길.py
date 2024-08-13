import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
mx = 0
for i in range(n-1):
    for j in range(i+1, n):
        if lst[j-1] >= lst[j]:
            break
        if lst[i] < lst[j]:
            if mx < lst[j] - lst[i]:
                mx = lst[j] - lst[i]
        else:
            break
print(mx)