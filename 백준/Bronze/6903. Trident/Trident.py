t = int(input())
s = int(input())
h = int(input())
for i in range(t):
    print('*'+' '*s+'*'+' '*s+'*')
print('*'*s +'***'+ '*'*s)
for k in range(h):
    print(' '*(s+1)+'*')