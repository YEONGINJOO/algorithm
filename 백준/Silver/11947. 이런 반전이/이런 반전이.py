import sys
input = sys.stdin.readline

def banjeon(a):
    st_a = str(a)
    banjeon_num = ''
    for i in range(len(st_a)):
        banjeon_num += str(9 - int(st_a[i]))
    return int(banjeon_num)

t = int(input())
for _ in range(t):
    n = int(input())
    st_n = str(n)
    if n % 10 == 0:
        print(n * banjeon(n))
    else:
        if n < 5 * (10 ** (len(st_n)-1)):
            print(n* banjeon(n))
        else:
            a = 5 * (10 ** (len(st_n)-1))
            print(a * banjeon(a))