lst = list(map(int, input().split()))
lst.sort()
x = input()
A = lst[0]
B = lst[1]
C = lst[2]
for i in x:
    if i == 'A':
        print(A, end=' ')
    elif i == 'B':
        print(B, end=' ')
    else:
        print(C, end=' ')