"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        p = prev = head
        ptr = head.next
        temp = None
        
        #create the copies
        while prev:
            new = Node(prev.val)
            temp = prev.next
            prev.next = new
            new.next = temp
            prev = prev.next.next
        
        head = p
        #make the random pointers assigned
        while head:
            if head.random is None:
                head.next.random = None
            else:
                rand = head.random.next
                head.next.random = rand            
            head = head.next.next
        
        head = p
        #unweaving the list
        l1,l2 = p , p.next
        newhead = l2
        
        while l1:
            temp = l1.next.next
            if l2.next:
                temp2 = l2.next.next
            else:
                temp2 = None
            l1.next = temp
            l2.next = temp2
            
            
            l2 = l2.next
            l1 = l1.next
        return newhead
        
            