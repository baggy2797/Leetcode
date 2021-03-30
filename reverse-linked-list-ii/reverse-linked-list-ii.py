# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        for i in range(0,left-1):
            pre = pre.next
        
        # print(pre)
        reverse = None
        curr = pre.next
        
        for i in range(right-left+1):
            next = curr.next
            curr.next = reverse
            reverse = curr
            curr = next
            
        pre.next.next = curr
        pre.next = reverse
        
        return dummy.next
        
                
            
        
        
        
            
        
        
        
        
        
        
            
        