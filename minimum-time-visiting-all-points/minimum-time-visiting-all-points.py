class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        slope = 0
        for i in range(len(points)-1):
            first,second = points[i],points[i+1]
            x1,y1 = first[0],first[1]
            x2,y2 = second[0],second[1]
            
            slope = slope + max(abs(y2-y1),abs(x2-x1))
        return slope
            
#             if slope == 1:
#                 #move ahead diagonally
#                 while x1<=x2 and y1<=y2:
#                     seconds = seconds+1
#                     x1=x1+1
#                     y1=y1+1
                
#             else:
#                 #move diagonally till either x+1 == goal of or y+1 == goal of y
#                 while x1<=x2 or y1<=y2 :
#                     seconds = seconds+1
#                     x1=x1+1
#                     y1=y1+1
                
#                 temp1,temp2 = 0,0
#                 while x1!=x2:
#                     temp1 = temp1+1
#                     x1 = x1+1
                
#                 while y1!=y2:
#                     temp2 = temp2+1
#                     y1=y1+1
                    
                    
                    
                    
                
                    
        