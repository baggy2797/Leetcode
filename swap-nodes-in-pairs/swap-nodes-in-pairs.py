# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(0)
        res.next = head
        prev_node = res
            
        while head and head.next:
            first = head
            second = head.next
            
            prev_node.next = second
            first.next = second.next
            second.next = first
            
            prev_node = first
            head = first.next
            
        return res.next
            