# Share
# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:


# Input: [1,2,3,0,2]
# Output: 3  cant go 1-3 0-2 bc of cooldown!
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

def maxProfit(prices):
    # buying brings us negative so we need to have something even more neg
    T_i11, T_i21 = float('-inf'), float('-inf')
    T_i10, T_i20 = 0, 0
    for p in prices:
        import pdb; pdb.set_trace()
        # seq of events is bottom to top (buy sell buy sell)
        T_i20 = max(T_i20, T_i21 + p)
        T_i21 = max(T_i21, T_i10 - p)
        T_i10 = max(T_i10, T_i11 + p)
        # T_i00 = 0
        T_i11 = max(T_i11, - p)
    
    return T_i20

# T[i][k][0] = max profit that could be gained on "i"_th day,
#             allowed "k" transactions, 
#             and at end of day, you have 0 stocks in hand

print (maxProfit( [3,3,5,0,0,3,1,4] ))