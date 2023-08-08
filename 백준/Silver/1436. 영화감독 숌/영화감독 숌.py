N = int(input())
cnt = 0
i = 666
ans_lst = []
while True:
    if '666' in str(i):
        cnt += 1
        if cnt == N:
            ans_lst.append(i)
            break
    i += 1
print(ans_lst[-1])