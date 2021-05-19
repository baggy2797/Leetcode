# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def merger(l1,l2):
            if l1 is None:
                return l2
            elif l2 is None:
                return l1
            elif l1.val<= l2.val:
                l1.next = merger(l1.next,l2)
                return l1
            else:
                l2.next = merger(l1,l2.next)
                return l2
        
        while len(lists)>=2:
            a1 = lists.pop(0)
            a2 = lists.pop(0)
            merged = merger(a1,a2)
            lists.append(merged)
        
        if lists:return lists[0]
        return None
        
    