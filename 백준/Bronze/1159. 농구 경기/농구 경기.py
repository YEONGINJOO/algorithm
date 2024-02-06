n = int(input())
lst = [input() for _ in range(n)]
ans = ''
for i in range(n):
    cnt = 0
    for j in range(n):
        if lst[i][0] == lst[j][0]:
            cnt += 1
            if cnt >= 5:
                if lst[i][0] in ans:
                    continue
                else:
                    ans += lst[i][0]
sol = ''
if ans == '':
    print('PREDAJA')
else:
    for i in sorted(ans):
        sol += i
    print(sol)