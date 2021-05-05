# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # dummy = ListNode(0)
        # ptr = dummy
        # nextPtr = head.next
        
        def reverseList(head):
            curr = None
            while head:
                temp = head.next
                head.next = curr
                curr = head
                head = temp
            return curr
        
        head = (reverseList(head))
        
        temp = head
        prev = temp
        # print(type(temp),temp.val)
        carry = 1
        
        while temp:
            res = temp.val + carry
            
            if res > 9:
                res = res -10
                carry = 1
            else:
                carry = 0
            temp.val = res
            if temp.next is None:
                prev = temp
            temp = temp.next
        
        if carry ==1 :
            dummy = ListNode(carry)
            prev.next = dummy
        
        
        return reverseList(head)
    
        
        
        