def maxScore(nums):
    n = len(nums)
    nums.insert(0, 1)
    nums.append(1)
    n = len(nums)
    bt = [[0 for x in range(n)] for x in range(n)]
    for b in range(2, n):
        for i in range(1, n-b + 1):
            j = i + b-1
            for a in range(i, j):
                cnt = nums[i-1]*nums[a]*nums[j] + bt[i][a] + bt[a + 1][j]
                if cnt > bt[i][j]:
                    bt[i][j] = cnt
    return bt[1][n-1]