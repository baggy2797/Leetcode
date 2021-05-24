# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:return head
        # Create a dummy node
        dummy = ListNode(-1)
        dummy.next = head
        
        first = dummy
        
        # Move over n nodes including dummy
        for i in range(n - 1):
            head = head.next
            
        # Increment ptrs till you reach end of list
        while head.next:
            first, head = first.next, head.next
            
        # Now first.next points to the nth node from the end
        first.next = first.next.next
        
        return dummy.next