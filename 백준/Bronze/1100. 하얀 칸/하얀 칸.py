lst = [input() for _ in range(8)]
cnt = 0
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if i % 2 == 0 and j % 2 == 0 and lst[i][j] == 'F':
            cnt += 1
        elif i % 2 == 1 and j % 2 == 1 and lst[i][j] == 'F':
            cnt += 1
print(cnt)