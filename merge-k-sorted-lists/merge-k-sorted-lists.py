# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = []
        for lis in lists:
            temp = lis
            while temp:
                # print(temp.val)
                res.append(temp.val)
                temp = temp.next
        # print(sorted(res))
        length = len(res)
        res = sorted(res)
        i = 0
        new2 = new1 = ListNode(0)
        while length:
            new1.next = ListNode(res[i])
            new1 = new1.next
            length = length-1
            i = i+1
        return (new2.next)
            
        