n = list(input())
cnt = 0
cntarr = [0] * 10
for i in range(len(n)):
    cntarr[int(n[i])] += 1
sm = cntarr[9] + cntarr[6]
if sm % 2 != 0:
    sm = sm // 2 + 1
else:
    sm = sm // 2
cntarr[9], cntarr[6] = sm, sm
print(max(cntarr))