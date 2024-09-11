import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    score_lst = [[h+1, 0, 0, 0] for h in range(n)]
    arr = [list(map(int, input().split())) for _ in range(m)]
    temp = []
    for j in range(1, m-1):
        if arr[-j][0] not in temp:
            temp.append(arr[-j][0])
            score_lst[arr[-j][0]-1][3] += j
    arr.sort()
    for i in range(m):
        if i != m - 1 and arr[i][0] == arr[i + 1][0]:
            if arr[i][1] != arr[i+1][1]:
                score_lst[arr[i][0] - 1][1] += arr[i][2]
        else:
            score_lst[arr[i][0]-1][1] += arr[i][2]
        score_lst[arr[i][0]-1][2] += 1
    score_lst.sort(key= lambda x: (-x[1], x[2], -x[3]))
    ans = 0
    for l in range(n):
        if score_lst[l][0] == t:
            ans = l + 1
            break
    print(ans)