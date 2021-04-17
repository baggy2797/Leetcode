# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        
        head1 = head
        length = 0
        while head1:
            length+=1
            head1 = head1.next
        
        result = head
        for i in range(k%length):
            result = self.rotateOnce(result)
        return result
        
    def rotateOnce(self,head):
        start = head
        first = head.next
        second = head
        while first.next:
            second = first
            first = first.next     
        second.next = None
        first.next = head
        start = first
        return start   