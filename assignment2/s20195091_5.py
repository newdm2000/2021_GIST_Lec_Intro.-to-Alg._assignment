def search(heights):
    m = len(heights)
    n = len(heights[0])
    
    # insert zeros
    for i in range(len(heights)):
        heights[i].append(0)
        heights[i].insert(0, 0)
    __zeros__ = [0 for col in range(len(heights[0]))]
    heights.insert(0, __zeros__)
    heights.append(__zeros__)
    
    
    
    c_list = [[False for col in range(len(heights[0]))] for row in range(heights)]
    e_list = [[False for col in range(len(heights[0]))] for row in range(heights)]
    stack = []
    
    for i in range(1, n+1):
        c_list[1][i] = True
        stack.append((1, i))
        
    for i in range(2, m+1):
        c_list[i][1] = True
        stack.append((i, 1))
    
    while stack:
        a = stack.pop()
        h = heights[a[0]][a[1]]
        if h <= heights[a[0]-1][a[1]]:
            
        if h <= heights[a[0]][a[1]]:
        
        if h <= heights[a[0]][a[1]]:
        
        if h <= heights[a[0]][a[1]]:
