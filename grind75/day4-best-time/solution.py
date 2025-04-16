import pdb

def max_profit(prices):
    max_profit=0
    for index in range(len(prices)):
        for jindex in range(index, len(prices)):
            if prices[jindex] - prices[index] > max_profit:
                max_profit = prices[jindex] - prices[index]

    return max_profit

if __name__=='__main__':
    prices=[7,6,4,3,1]
    profit = max_profit(prices)
    print(profit)
