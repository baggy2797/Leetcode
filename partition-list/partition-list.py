class Solution(object):
    def partition(self, head, x):
        h1 = greater =ListNode(0)
        h2 = lesser = ListNode(0)
        
        temp = head
        while temp:
            
            if temp.val < x:
                lesser.next = temp
                lesser = lesser.next
            else:
                greater.next = temp
                greater = greater.next
            temp = temp.next
        

        greater.next =None
        
        lesser.next = h1.next
        
        return (h2.next)
        
        
            