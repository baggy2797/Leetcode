class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0]*len(boxes)
        dp1,dp2 = [0]*len(boxes),[0]*len(boxes)
        leftcount,rightcount = int(boxes[0]),int(boxes[-1])
        #going leftwards
        dp1[0] = 0
        dp2[len(boxes)-1] = 0
        for i in range(1,len(boxes)):
            dp1[i] = dp1[i-1]+leftcount
            if boxes[i] =="1":
                leftcount = leftcount+1
        
        for j in range(len(boxes)-2,-1,-1):
            dp2[j] = dp2[j+1]+rightcount
            if boxes[j] == "1":
                rightcount = rightcount+1
        
        for k in range(len(boxes)):
            res[k] = dp1[k]+ dp2[k]
        
        return res
            
#         res = [0]*len(boxes)
    
#         for i in range(len(boxes)):
#             l = 0
#             temp = 0
#             while l<len(boxes):
#                 if boxes[l] =='1':
#                     temp = temp + abs(l-i)
#                 l = l+1
#             res[i] = temp
        
#         return (res)
                    
                
                
        