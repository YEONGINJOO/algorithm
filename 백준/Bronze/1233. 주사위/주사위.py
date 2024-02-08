s1, s2, s3 = map(int, input().split())
s1_lst = [i for i in range(1,s1+1)]
s2_lst = [i for i in range(1,s2+1)]
s3_lst = [i for i in range(1,s3+1)]
lst = []
for i in range(s1):
    for j in range(s2):
        for k in range(s3):
            lst.append(s1_lst[i]+s2_lst[j]+s3_lst[k])

cnt_lst = [0] * 81
for i in range(len(lst)):
    cnt_lst[lst[i]] += 1
mx = 0
ans = 0
for i in range(len(cnt_lst)):
    if cnt_lst[i] > mx:
        mx = cnt_lst[i]
        ans = i
print(ans)