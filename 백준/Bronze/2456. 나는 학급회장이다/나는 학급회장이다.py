import sys
input = sys.stdin.readline
n = int(input())
a_cnt = [0] * 4
b_cnt = [0] * 4
c_cnt = [0] * 4
for _ in range(n):
    a, b, c = map(int, input().split())
    a_cnt[0] += a
    a_cnt[a] += 1
    b_cnt[0] += b
    b_cnt[b] += 1
    c_cnt[0] += c
    c_cnt[c] += 1

if a_cnt[0] > b_cnt[0] and a_cnt[0] > c_cnt[0]:
    print(1, max(a_cnt[0], b_cnt[0], c_cnt[0]))
elif b_cnt[0] > a_cnt[0] and b_cnt[0] > c_cnt[0]:
    print(2, max(a_cnt[0], b_cnt[0], c_cnt[0]))
elif c_cnt[0] > a_cnt[0] and c_cnt[0] > b_cnt[0]:
    print(3, max(a_cnt[0], b_cnt[0], c_cnt[0]))
elif a_cnt[0] == max(a_cnt[0], b_cnt[0], c_cnt[0]) and a_cnt[0] == b_cnt[0] and a_cnt[0] > c_cnt[0]:
    if a_cnt[3] > b_cnt[3]:
        print(1, max(a_cnt[0], b_cnt[0], c_cnt[0]))
    elif a_cnt[3] < b_cnt[3]:
        print(2, max(a_cnt[0], b_cnt[0], c_cnt[0]))
    else:
        if a_cnt[2] > b_cnt[2]:
            print(1, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        elif a_cnt[2] < b_cnt[2]:
            print(2, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        else:
            print(0, max(a_cnt[0], b_cnt[0], c_cnt[0]))
elif a_cnt[0] == max(a_cnt[0], b_cnt[0], c_cnt[0]) and a_cnt[0] == c_cnt[0] and a_cnt[0] > b_cnt[0]:
    if a_cnt[3] > c_cnt[3]:
        print(1, max(a_cnt[0], b_cnt[0], c_cnt[0]))
    elif a_cnt[3] < c_cnt[3]:
        print(3, max(a_cnt[0], b_cnt[0], c_cnt[0]))
    else:
        if a_cnt[2] > c_cnt[2]:
            print(1, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        elif a_cnt[2] < c_cnt[2]:
            print(3, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        else:
            print(0, max(a_cnt[0], b_cnt[0], c_cnt[0]))
elif b_cnt[0] == max(a_cnt[0], b_cnt[0], c_cnt[0]) and b_cnt[0] == c_cnt[0] and b_cnt[0] > a_cnt[0]:
    if b_cnt[3] > c_cnt[3]:
        print(2, max(a_cnt[0], b_cnt[0], c_cnt[0]))
    elif b_cnt[3] < c_cnt[3]:
        print(3, max(a_cnt[0], b_cnt[0], c_cnt[0]))
    else:
        if b_cnt[2] > c_cnt[2]:
            print(2, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        elif b_cnt[2] < c_cnt[2]:
            print(3, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        else:
            print(0, max(a_cnt[0], b_cnt[0], c_cnt[0]))
elif a_cnt[0] == b_cnt[0] and a_cnt[0] == c_cnt[0]:
    if a_cnt[3] > b_cnt[3] and a_cnt[3] > c_cnt[3]:
        print(1, max(a_cnt[0], b_cnt[0], c_cnt[0]))
    elif b_cnt[3] > a_cnt[3] and b_cnt[3] > c_cnt[3]:
        print(2, max(a_cnt[0], b_cnt[0], c_cnt[0]))
    elif c_cnt[3] > a_cnt[3] and c_cnt[3] > b_cnt[3]:
        print(3, max(a_cnt[0], b_cnt[0], c_cnt[0]))
    elif a_cnt[3] == max(a_cnt[3], b_cnt[3], c_cnt[3]) and a_cnt[3] == b_cnt[3] and a_cnt[3] > c_cnt[3]:
        if a_cnt[2] > b_cnt[2]:
            print(1, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        elif a_cnt[2] < b_cnt[2]:
            print(2, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        else:
            print(0, max(a_cnt[0], b_cnt[0], c_cnt[0]))
    elif a_cnt[3] == max(a_cnt[3], b_cnt[3], c_cnt[3]) and a_cnt[3] == c_cnt[3] and a_cnt[3] > b_cnt[3]:
        if a_cnt[2] > c_cnt[2]:
            print(1, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        elif a_cnt[2] < c_cnt[2]:
            print(3, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        else:
            print(0, max(a_cnt[0], b_cnt[0], c_cnt[0]))
    elif b_cnt[3] == max(a_cnt[3], b_cnt[3], c_cnt[3]) and b_cnt[3] == c_cnt[3] and b_cnt[3] > a_cnt[3]:
        if b_cnt[2] > c_cnt[2]:
            print(2, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        elif b_cnt[2] < c_cnt[2]:
            print(3, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        else:
            print(0, max(a_cnt[0], b_cnt[0], c_cnt[0]))
    elif a_cnt[3] == b_cnt[3] and a_cnt[3] == c_cnt[3]:
        if a_cnt[2] > b_cnt[2] and a_cnt[2] > c_cnt[2]:
            print(1, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        elif b_cnt[2] > a_cnt[2] and b_cnt[2] > c_cnt[2]:
            print(2, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        elif c_cnt[2] > a_cnt[2] and c_cnt[2] > b_cnt[2]:
            print(3, max(a_cnt[0], b_cnt[0], c_cnt[0]))
        else:
            print(0, max(a_cnt[0], b_cnt[0], c_cnt[0]))
else:
    print(0, max(a_cnt[0], b_cnt[0], c_cnt[0]))