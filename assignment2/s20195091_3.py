def budget(evaluation):
    profit = len(evaluation)
    stt = 1
    min_idx = 0
    max_idx = 0
    for i in range(len(evaluation)):
        if i == 0:
            if  evaluation[i] > evaluation[i+1]:
                profit = profit + 1
                max_idx = -1
        elif i == len(evaluation)-1:
            if evaluation[i-1] < evaluation[i]:
                profit = profit + i - min_idx
        else:
            if evaluation[i-1] < evaluation[i] and evaluation[i] <= evaluation[i+1]:
                profit = profit + i - min_idx
            elif evaluation[i-1] > evaluation[i] and evaluation[i] > evaluation[i+1]:
                profit = profit + i - max_idx
            elif evaluation[i-1] < evaluation[i] and evaluation[i] > evaluation[i+1]:
                profit = profit + i - min_idx
                max_idx = i
            elif evaluation[i-1] > evaluation[i] and evaluation[i] < evaluation[i+1]:
                min_idx = i
            elif evaluation[i-1] == evaluation[i] and evaluation[i] > evaluation[i+1]:
                max_idx = i-1
                profit = profit + 1
            elif evaluation[i-1] == evaluation[i] and evaluation[i] < evaluation[i+1]:
                min_idx = i
            else:
                pass
    return profit * 1000

print(budget([1,2,3,4,6,4,3,1,2,7,6,4,3,3,2,1,1,2,2,2,4,3]))
