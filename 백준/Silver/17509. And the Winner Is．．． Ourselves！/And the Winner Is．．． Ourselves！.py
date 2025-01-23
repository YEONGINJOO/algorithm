import sys
input = sys.stdin.readline
penalty = 0
prob = []
for _ in range(11):
    d, v = map(int, input().split())
    prob.append([d, v])
prob.sort()
ct = 0
for d, v in prob:
    penalty += ct + d + 20 *v
    ct += d
print(penalty)