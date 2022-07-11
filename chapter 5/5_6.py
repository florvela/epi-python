# buy and sell a stock once

def max_profit(prices):
    min_so_far = float('inf')
    max_so_far = 0

    for price in prices:
        min_so_far = min(price, min_so_far)
        max_so_far = max(price - min_so_far, max_so_far)

    return max_so_far

print(max_profit([310,315,275,295,260,270,290,230,255,250])) # 30