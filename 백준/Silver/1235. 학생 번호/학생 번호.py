n = int(input())
lst = [input() for _ in range(n)]
mn = 1001
for i in range(len(lst[0])):
    cnt = 0
    for j in range(n):
        for k in range(n):
            if j != k:
                if lst[j][len(lst[0])-1-i:] == lst[k][len(lst[0])-1-i:]:
                    cnt += 1
        if cnt >= 1:
            break
    if cnt == 0:
        if mn > i:
            mn = i
        break
print(mn+1)