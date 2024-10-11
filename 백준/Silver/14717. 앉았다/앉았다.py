import sys
input = sys.stdin.readline
A, B = map(int, input().split())
A_lst = [i for i in range(1, 11)]
B_lst = [i for i in range(1, 11)]
A_lst.remove(A)
B_lst.remove(B)
sm = A_lst + B_lst
all = 153
cnt = 0
s = int(str(A + B)[-1])
for i in range(len(sm)):
    for j in range(i+1, len(sm)):
        if A == B:
            if sm[i] == sm[j] and sm[i] > A:
                cnt += 1
        else:
            if sm[i] == sm[j]:
                cnt += 1
            else:
                if s <= int(str(sm[i] + sm[j])[-1]):
                    cnt += 1
print(f'{(all-cnt)/all:.3f}')