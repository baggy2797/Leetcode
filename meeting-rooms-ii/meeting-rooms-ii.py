class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        if not intervals:
            return 0
        
        usedRooms = 0
        
        startTimings = sorted([i[0] for i in intervals])
        endTimings = sorted([i[1] for i in intervals])
        
        end = 0
        start = 0
        
        while start < length:
            if startTimings[start] >= endTimings[end]:
                usedRooms-=1
                end+=1
            
            usedRooms+=1
            start+=1
        
        return usedRooms
            
            
            
        
            
                    
            
            