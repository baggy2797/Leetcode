"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.seen = {}
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        
        if head in self.seen:
            return self.seen[head]
        
        node = Node(head.val,None,None)
        
        self.seen[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node
        
        