def budget(evaluation):
    profit = len(evaluation)
    min_idx = 0
    max_idx = 0
    idx = 100000
    for i in range(len(evaluation)):
        if i == 0:
            if  evaluation[i] > evaluation[i+1]:
                profit = profit + 1
                max_idx = -1
                
        elif i == len(evaluation)-1:
            if evaluation[i-1] < evaluation[i]:
                profit = profit + i - min_idx
            elif evaluation[i-1] >= evaluation[i]:
                if idx <= (i - max_idx - 1):
                    profit = profit - idx + i - max_idx
                    idx = 100000
                else:
                    pass
            else:
                pass
                
        else:
            if evaluation[i-1] < evaluation[i] and evaluation[i] <= evaluation[i+1]:
                profit = profit + i - min_idx
            elif evaluation[i-1] > evaluation[i] and evaluation[i] > evaluation[i+1]:
                profit = profit + i - max_idx
            elif evaluation[i-1] < evaluation[i] and evaluation[i] > evaluation[i+1]:
                profit = profit + i - min_idx
                idx = i - min_idx
                max_idx = i
            elif evaluation[i-1] > evaluation[i] and evaluation[i] < evaluation[i+1]:
                min_idx = i
                if idx <= (i - max_idx - 1):
                    profit = profit - idx + i - max_idx
                    idx = 100000
                else:
                    pass
            elif evaluation[i-1] > evaluation[i] and evaluation[i] == evaluation[i+1]:
                if idx <= (i - max_idx - 1):
                    profit = profit - idx + i - max_idx
                    idx = 100000
                else:
                    pass
            elif evaluation[i-1] == evaluation[i] and evaluation[i] > evaluation[i+1]:
                max_idx = i-1
                profit = profit + 1
            elif evaluation[i-1] == evaluation[i] and evaluation[i] < evaluation[i+1]:
                min_idx = i
            else:
                pass
    return profit * 1000