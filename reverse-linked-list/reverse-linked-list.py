# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        count,stack = 0,[]
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        count = len(stack)
        temp = head
        
        while count:
            head.val = stack.pop(-1)
            head = head.next
            count = count - 1

        return temp