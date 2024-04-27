n, m = map(int, input().split())
music_lst = [input().split() for _ in range(n)]
um = [input().split() for _ in range(m)]
for i in range(m):
    cnt = 0
    ans = ''
    for j in range(n):
        if um[i] == music_lst[j][2:5]:
            cnt += 1
            ans = music_lst[j][1]
    if cnt == 1:
        print(ans)
    elif cnt > 1:
        print('?')
    else:
        print('!')