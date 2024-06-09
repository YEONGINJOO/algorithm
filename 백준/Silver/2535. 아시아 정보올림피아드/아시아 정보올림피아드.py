import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
lst = [0] * (arr[n-1][0]+1)
arr.sort(key=lambda x : x[2], reverse=True)
cnt = 0
for i in range(n):
    if lst[arr[i][0]] == 2:
        continue
    else:
        lst[arr[i][0]] += 1
        print(f'{arr[i][0]} {arr[i][1]}')
        cnt += 1
    if cnt == 3:
       break