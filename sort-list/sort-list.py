# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        def mergeSort(head):
            if head is None or head.next is None:return head
            left = slow = fast = head
            fast = fast.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            right = slow.next
            slow.next = None
            
            left_sorted = mergeSort(left)
            right_sorted = mergeSort(right)
            
            return mergeHalves(left_sorted,right_sorted)
            
        def mergeHalves(l1,l2):
            dummy = ListNode()
            prev = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next
            prev.next = l1 or l2
            
            return dummy.next
        
        return mergeSort(head)
                
                