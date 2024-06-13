import sys
input = sys.stdin.readline

n = int(input())
lst = [sys.stdin.readline().strip() for _ in range(n)]
m = int(input())
arr = [sys.stdin.readline().strip() for _ in range(m)]
fst_str = ''
last_str = ''
ans = ''
if n == 1:
    print(arr[0])
else:
    for i in range(n):
        if lst[i] == '?' and i == 0:
            last_str = lst[i+1][0]
            for j in range(m):
                if arr[j] not in lst and arr[j][-1] == last_str:
                    ans = arr[j]
                    break
        elif lst[i] == '?' and i == n-1:
            fst_str = lst[i - 1][-1]
            for j in range(m):
                if arr[j] not in lst and arr[j][0] == fst_str:
                    ans = arr[j]
                    break
        elif lst[i] =='?':
            fst_str = lst[i - 1][-1]
            last_str = lst[i + 1][0]
            for j in range(m):
                if arr[j] not in lst and arr[j][0] == fst_str and arr[j][-1] == last_str:
                    ans = arr[j]
                    break
    print(ans)