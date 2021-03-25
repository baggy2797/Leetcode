class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        dictA = {}
        for i in range(len(A)):
            if A[i] not in dictA:
                dictA[A[i]] = 1
            else:
                dictA[A[i]]+=1
        
        maximum = (-1)*(sys.maxsize)
        # print(dictA)
        post_sort = sorted(dictA.items())
        for val in post_sort[::-1]:
            if val[1] == 1:
                return val[0]
        return -1
            
        