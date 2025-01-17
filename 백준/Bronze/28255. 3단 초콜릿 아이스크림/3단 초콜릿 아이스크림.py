import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a = input().strip()
    if len(a) % 3 == 0:
        a1 = a[:len(a)//3]
    else:
        a1 = a[:len(a)//3+1]
    if a1 + a1[::-1] + a1 == a:
        print(1)
    elif a1 +  a1[::-1][1:] + a1 == a:
        print(1)
    elif a1 + a1[::-1] + a1[1:] == a:
        print(1)
    elif a1 + a1[::-1][1:] + a1[1:] == a:
        print(1)
    else:
        print(0)