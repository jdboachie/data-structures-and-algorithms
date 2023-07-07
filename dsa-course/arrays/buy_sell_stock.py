def buy_and_sell_stock_once(prices):
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        diff = price - min_price
        max_profit = max(max_profit, diff)
    return max_profit


assert buy_and_sell_stock_once(
    [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 30
print(".", end="")
assert buy_and_sell_stock_once([50, 40, 30, 20, 10]) == 0
print(".", end="")
assert buy_and_sell_stock_once([110, 215, 180, 335, 5]) == 225
print(".", end="")
assert buy_and_sell_stock_once([100, 180, 260, 310, 40, 535, 695]) == 655
print(".")
print("OK.")
