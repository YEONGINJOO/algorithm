T = int(input())
for _ in range(T):
    G, C, E = map(int, input().split())
    if G == 1:
        if C > E:
            print(0)
        else:
            print(E-C)
    elif G == 2:
        if C > E:
            print(0)
        else:
            print((E-C)*3)
    else:
        if C > E:
            print(0)
        else:
            print((E-C)*5)