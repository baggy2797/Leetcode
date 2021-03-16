# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next =None
        res = dummy
        num1,num2 = "",""
        while l1:
            num1 = num1 + str(l1.val)
            l1 = l1.next
    
        while l2:
            num2 = num2 + str(l2.val)
            l2 = l2.next
        
        num3 = int(num1) + int(num2)
        num3 = str(num3)
        i = 0
        while i < len(num3):
            temp = num3[i]
            res.next = ListNode(temp)
            res = res.next
            i = i+1
            
        return dummy.next
        
        
        