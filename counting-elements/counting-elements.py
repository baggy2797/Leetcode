class Solution:
    def countElements(self, arr: List[int]) -> int:
        if len(arr) <2:
            return 0
        
        count = 0
        for i in range(len(arr)):
            check = arr[i]+1
            if check in arr:
                count = count+1 
                # arr[i] = -1
                # arr[arr.index(check)] = -1
        return (count)
        