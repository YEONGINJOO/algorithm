T = int(input())
for _ in range(T):
    a = input()
    cnt = 0
    for i in a:
        if i == 'D':
            break
        else:
            cnt += 1
    print(cnt)