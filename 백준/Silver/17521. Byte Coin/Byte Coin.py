import sys
input = sys.stdin.readline
n, w = map(int, input().split())
prices = [int(input()) for _ in range(n)]

cash = w
coins = 0

for i in range(n - 1):
    # 내일 가격이 오늘보다 비쌀 때: 오늘 사기
    if prices[i + 1] > prices[i]:
        buy = cash // prices[i]
        coins += buy
        cash -= buy * prices[i]
    # 내일 가격이 오늘보다 싸거나 같을 때: 오늘 팔기
    elif prices[i + 1] < prices[i]:
        cash += coins * prices[i]
        coins = 0

# 마지막 날 무조건 다 판다
cash += coins * prices[-1]

print(cash)