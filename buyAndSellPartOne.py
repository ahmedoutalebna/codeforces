def maxProfit(prices):
    # buy_price = prices[0]
    # profit = 0
    #
    # for p in prices[1:]:
    #     if buy_price > p:
    #         buy_price = p
    #     profit = max(profit, p - buy_price)
    buy_price = prices[0]
    max_profit = 0
    for p in prices[1:]:
        if p > buy_price:
            max_profit += (p - buy_price)
        buy_price = p

    return max_profit

print(maxProfit([7,6,4,3,1]))