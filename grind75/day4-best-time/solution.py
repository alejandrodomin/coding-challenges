import pdb

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

if __name__=='__main__':
    prices=[7,2,7,13,1,5,3,6,4]
    profit = max_profit(prices)
    print(profit)
