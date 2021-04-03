import heapq
class Solution:
    def minDifference(self, A):
        # 1) Trivial case
        if len(A)<=4:
            return 0
        #
        # 2) Fetch the top-4 elements at each extreme
        big   = heapq.nlargest(4,A)[::-1]
        small = heapq.nsmallest(4,A)
        #
        # 4) Find the optimal answer
        return min([ (big[-4+i] - small[i]) for i in range(4) ])
        