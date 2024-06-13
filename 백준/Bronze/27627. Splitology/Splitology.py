import sys

a = sys.stdin.readline().strip()
ans = ''
for i in range(len(a)-1):
    st1 = a[:i+1]
    st2 = a[i+1:]
    if st1 == st1[::-1] and st2 == st2[::-1]:
        print(st1, st2)
        break
else:
    print('NO')