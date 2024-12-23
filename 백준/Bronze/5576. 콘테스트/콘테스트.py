import sys
input = sys.stdin.readline
w = []
k = []
for i in range(20):
    s = int(input())
    if i < 10:
        w.append(s)
    else:
        k.append(s)
w.sort()
k.sort()
print(sum(w[7:]), sum(k[7:]))