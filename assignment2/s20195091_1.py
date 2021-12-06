import heapq

def sorted_list(lists):
    K = len(lists)
    s_list = []
    heap = []
    
    for i in range(0, K):
        heapq.heappush(heap, (lists[i][0], i))
    
    while len(heap)>0:
        j = heapq.heappop(heap)
        q = j[1]
        a = lists[q].pop(0)
        s_list.append(a)
        if len(lists[q]) != 0:
            heapq.heappush(heap, (lists[q][0], q))
        else:
            
            pass
    
    return s_list
