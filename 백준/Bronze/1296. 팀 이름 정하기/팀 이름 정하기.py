a = input()
n = int(input())
lst = [input() for _ in range(n)]
lst.sort()
cnt = [[0] * 4 for _ in range(n)]
for i in range(n):
    for j in lst[i]:
        if j == 'L':
            cnt[i][0] += 1
        elif j == 'O':
            cnt[i][1] += 1
        elif j == 'V':
            cnt[i][2] += 1
        elif j == 'E':
            cnt[i][3] += 1
    for k in range(len(a)):
        if a[k] == 'L':
            cnt[i][0] += 1
        elif a[k] == 'O':
            cnt[i][1] += 1
        elif a[k] == 'V':
            cnt[i][2] += 1
        elif a[k] == 'E':
            cnt[i][3] += 1
mx = 0
ans = 0
for i in range(n):
    mull = 1
    for j in range(4):
        for k in range(j+1, 4):
            mull *= (cnt[i][j] + cnt[i][k])
    b = mull % 100
    if b > mx:
        mx = b
        ans = i
print(lst[ans])