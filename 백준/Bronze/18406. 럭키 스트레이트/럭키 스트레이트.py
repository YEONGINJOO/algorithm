n = int(input())
a = str(n)
a1 = a[:len(a)//2]
a2 = a[len(a)//2:]
sm1 = sm2 = 0
for i in range(len(a)//2):
    sm1 += int(a1[i])
    sm2 += int(a2[i])
if sm1 == sm2:
    print('LUCKY')
else:
    print('READY')