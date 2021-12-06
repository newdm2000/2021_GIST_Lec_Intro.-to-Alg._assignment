def max_profit(cost):
    min = 10000
    profit = 0
    maxProfit = 0
    for i in range(1,len(cost)):
        if min > cost[i-1]: min = cost[i-1]
        profit = max(0, cost[i]-min)
        maxProfit = max(profit, maxProfit)
    return maxProfit

cost = [14,2,10,6,12,8]

print(max_profit(cost))