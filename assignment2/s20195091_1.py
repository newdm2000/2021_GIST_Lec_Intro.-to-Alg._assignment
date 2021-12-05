class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        data = []
        if len(lists) == 0: return None
            
        if len(lists) == 1: return lists[0]
            
        for lst in lists:
            if lst == None: continue
                
            data.append(lst.val)
            while lst.next: # 노드가 끝날 때까지 탐색
                lst = lst.next
                data.append(lst.val)

        lists = ListNode()
        if len(data) == 0: return None
        data.sort()
        
        for i in range(len(data)):
            if i == 0:
                lists.val = data[i]
            else:
                node = lists
                # node.next가 None 없을 때까지, 더 input할 엘리먼트가 없을 때까지
                while node.next: 
                    node = node.next
                node.next = ListNode(data[i])
                
        return lists