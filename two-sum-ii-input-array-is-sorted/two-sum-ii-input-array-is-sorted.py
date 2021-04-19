class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        length = len(numbers)
        start,end = 0 , length-1
        
        def binary_search(numbers, low, high, target,i):
            while high >= low:
                mid = (high + low) // 2
                if numbers[mid] == target:
                    if mid!=i:
                        return mid
                    else:
                        return mid+1
                elif numbers[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                return -1
        
        for i in range(length):
            search = target - numbers[i]
            idx = binary_search(numbers,start,end,search,i)
            if idx==-1:
                continue
            else:
                return [min(i,idx)+1,max(i,idx)+1]
