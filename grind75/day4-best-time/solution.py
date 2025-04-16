import pdb

def max_profit(prices):
    max_profit=0
    buy_ptr, sell_ptr=0,0
    
    while sell_ptr < len(prices):
        delta=prices[sell_ptr] - prices[buy_ptr]

        if delta > max_profit:
            max_profit = delta
        elif delta < 0:
            buy_ptr+=1
        else:
            sell_ptr+=1

    return max_profit

if __name__=='__main__':
    prices=[7,1,5,3,6,4]
    profit = max_profit(prices)
    print(profit)
