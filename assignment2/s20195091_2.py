def max_profit(cost):
    cost.append(0)
    tcost = 0
    k = 0
    for i in range(len(cost)-1):
        if cost[i] < cost[i+1] and k == 0:
            k = cost[i]
        elif cost[i] > cost[i+1] and k != 0:
            tcost = tcost + cost[i] - k
            k = 0
        else:
            pass
        
    return tcost
