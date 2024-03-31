a = input()
ans = 'NO'
if len(a) == 1:
    ans = 'NO'
else:
    for i in range(len(a)):
        temp1 = a[:i+1]
        temp2 = a[i+1:]
        mt1 = 1
        mt2 = 1
        for j in range(len(temp1)):
            mt1 *= int(temp1[j])
        for k in range(len(temp2)):
            mt2 *= int(temp2[k])
        if mt1 == mt2:
            ans = 'YES'
            break
print(ans)