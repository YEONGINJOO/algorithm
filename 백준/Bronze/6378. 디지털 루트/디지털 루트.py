import sys
input = sys.stdin.readline

def dr(a):
    if int(a) < 10:
        return int(a)
    else:
        temp = 0
        for i in a:
            temp += int(i)
        return dr(str(temp))

while True:
    n = int(input())
    if n == 0:
        break
    str_n = str(n)
    print(dr(str_n))
