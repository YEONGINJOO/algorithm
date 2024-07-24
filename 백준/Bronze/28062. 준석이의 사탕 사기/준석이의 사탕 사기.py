import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
sm = sum(lst)
i = 0
if sm % 2 == 0:
    print(sm)
else:
    while True:
        if sm == 0:
            print(0)
            break
        if sm % 2 != 0:
            sm -= lst[i]
            if sm % 2 != 0:
                sm += lst[i]
                i += 1
            else:
                print(sm)
                break