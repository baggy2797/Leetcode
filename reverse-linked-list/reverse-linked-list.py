# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        dummy = ListNode(None)
        # dummy.next = None
        temp = head
        
        
        while head:
            #for moving ahead in the loop
            ptr = head.next
            #create the. new link
            # head.next = None
            head.next = dummy
            #shift the dummy
            dummy = head
            #move ahead in loop
            head = ptr
        
        temp.next = None
        return dummy
        
            
        
        