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
    
    c_list = [[False for col in range(len(heights[0]))] for row in range(len(heights))]
    e_list = [[False for col in range(len(heights[0]))] for row in range(len(heights))]
    stack = []
    ll = []
    
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
            if c_list[a[0]-1][a[1]] == False:
                c_list[a[0]-1][a[1]] = True
                stack.append((a[0]-1, a[1]))
            
        if h <= heights[a[0]+1][a[1]]:
            if c_list[a[0]+1][a[1]] == False:
                c_list[a[0]+1][a[1]] = True
                stack.append((a[0]+1, a[1]))
        
        if h <= heights[a[0]][a[1]-1]:
            if c_list[a[0]][a[1]-1] == False:
                c_list[a[0]][a[1]-1] = True
                stack.append((a[0], a[1]-1))
        
        if h <= heights[a[0]][a[1]+1]:
                if c_list[a[0]][a[1]+1] == False:
                    c_list[a[0]][a[1]+1] = True
                    stack.append((a[0], a[1]+1))
    
    for i in range(1, n+1):
        e_list[m][i] = True
        stack.append((m, i))
        
    for i in range(1, m):
        e_list[i][n] = True
        stack.append((i, n))
    
    while stack:
        a = stack.pop()
        h = heights[a[0]][a[1]]
        if h <= heights[a[0]-1][a[1]]:
            if e_list[a[0]-1][a[1]] == False:
                e_list[a[0]-1][a[1]] = True
                stack.append((a[0]-1, a[1]))
            
        if h <= heights[a[0]+1][a[1]]:
            if e_list[a[0]+1][a[1]] == False:
                e_list[a[0]+1][a[1]] = True
                stack.append((a[0]+1, a[1]))
        
        if h <= heights[a[0]][a[1]-1]:
            if e_list[a[0]][a[1]-1] == False:
                e_list[a[0]][a[1]-1] = True
                stack.append((a[0], a[1]-1))
        
        if h <= heights[a[0]][a[1]+1]:
                if e_list[a[0]][a[1]+1] == False:
                    e_list[a[0]][a[1]+1] = True
                    stack.append((a[0], a[1]+1))
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(c_list[i][j] and e_list[i][j]):
                ll.append([i-1,j-1])
    
    return ll
    