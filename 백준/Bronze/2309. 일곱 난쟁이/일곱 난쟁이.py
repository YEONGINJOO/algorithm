import sys
input = sys.stdin.readline
lst = [int(input()) for _ in range(9)]
lst.sort()
sm = sum(lst)
for i in range(9):
    for j in range(i+1, 9):
        if sm - lst[i] - lst[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    pass
                else:
                    print(lst[k])
            exit()