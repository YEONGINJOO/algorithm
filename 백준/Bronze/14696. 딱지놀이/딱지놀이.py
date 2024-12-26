import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a, *a_p = map(int, input().split())
    b, *b_p = map(int, input().split())
    a_c = [0] * 5
    b_c = [0] * 5
    for i in a_p:
        a_c[i] += 1
    for j in b_p:
        b_c[j] += 1
    if a_c[4] > b_c[4]:
        print('A')
    elif a_c[4] < b_c[4]:
        print('B')
    else:
        if a_c[3] > b_c[3]:
            print('A')
        elif a_c[3] < b_c[3]:
            print('B')
        else:
            if a_c[2] > b_c[2]:
                print('A')
            elif a_c[2] < b_c[2]:
                print('B')
            else:
                if a_c[1] > b_c[1]:
                    print('A')
                elif a_c[1] < b_c[1]:
                    print('B')
                else:
                    print('D')