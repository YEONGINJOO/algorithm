import sys
input = sys.stdin.readline

N = int(input())
for k in range(1, N + 1):
    M = int(input())
    lst = list(map(int, input().split()))

    max_profit = 0
    best_buy_month = -1
    best_sell_month = -1

    for buy in range(11):  # 구매는 1~11월 (0~10 인덱스)
        for sell in range(buy + 1, 12):  # 판매는 구매 다음 달부터 12월까지

            buy_price = lst[buy]
            sell_price = lst[sell]
            
            if sell_price > buy_price:
                quantity = M // buy_price
                profit = (sell_price * quantity) - (buy_price * quantity)
                
                if profit > max_profit or (profit == max_profit and buy_price < lst[best_buy_month]):
                    max_profit = profit
                    best_buy_month = buy
                    best_sell_month = sell

    if max_profit > 0:
        print(f'Case #{k}: {best_buy_month + 1} {best_sell_month + 1} {max_profit}')
    else:
        print(f'Case #{k}: IMPOSSIBLE')
