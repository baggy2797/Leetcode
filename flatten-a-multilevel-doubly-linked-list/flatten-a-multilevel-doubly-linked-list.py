"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return
        ptr = head
        while head:
            # 'print(head.val)
            if head.child:
                tail = head.next
                # head.next = None
                temp = self.flatten(head.child)
                # print(temp)
                head.child = None
                head.next = temp
                temp.prev = head
                while temp.next:
                    temp = temp.next
                if tail:
                    temp.next = tail
                    tail.prev = temp
            
            head = head.next
        return ptr