class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0]*len(boxes)
        
        for i in range(len(boxes)):
            l = 0
            temp = 0
            while l<len(boxes):
                if boxes[l] =='1':
                    temp = temp + abs(l-i)
                l = l+1
            res[i] = temp
        return (res)
                    
                
                
        