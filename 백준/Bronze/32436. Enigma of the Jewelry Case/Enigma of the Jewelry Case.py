import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
flag = 0

while flag == 0:
    change_arr = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(arr[j][i])
        change_arr.append(temp)
    change_arr = change_arr[::-1]
    arr = change_arr
    cnt += 1
    for i in range(n-1):
        for j in range(n-1):
            if change_arr[i][j] < change_arr[i][j+1] and change_arr[j][i] < change_arr[j+1][i]:
                flag = 1
            else:
                flag = 0
                break
        break
if cnt == 4:
    print(0)
else:
    print(cnt)