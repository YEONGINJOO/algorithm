import sys
input = sys.stdin.readline
lst = [int(input()) for _ in range(10)]
sm = 0
for i in range(10):
    sm += lst[i]
    if sm >= 100: # 점수의 합이 100보다 크거나 같을 때
        if sm - 100 > 100 - (sm-lst[i]): # 합에서 100을 뺀것이 그전의 값과 비교했을 때 크다면
            sm -= lst[i] # 합에서 뺀다.
        break
print(sm)