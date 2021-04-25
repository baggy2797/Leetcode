# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        count = 0
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow!=fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None