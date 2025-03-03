# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists == []:
            return None
        if lists is None:
            return lists
        while len(lists) > 1:
            l1,l2 = lists.pop(0),lists.pop(0)
            lists.append(self.mergeTwoLists(l1,l2))
            
        return lists[0] if lists else []
        
    def mergeTwoLists(self,l1,l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2