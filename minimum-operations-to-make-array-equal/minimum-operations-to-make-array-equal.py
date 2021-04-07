class Solution:
    def minOperations(self, n: int) -> int:
        arr = [0]*(n)
        for i in range(len(arr)):
            arr[i] = (i*2)+1
        # print(arr)
        target = sum(arr)//n
        # print(target)
        left = 0
        right = len(arr)-1
        
        count = 0
        while left < right:
            count+= abs(arr[left]-target)
            left+=1
            right-=1
            
        return(count)
            