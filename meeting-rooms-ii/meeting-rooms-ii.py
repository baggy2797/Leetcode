class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals is None:
            return 0
        start,end = [],[]
        
        length = len(intervals)
        
        for i in range(length):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
            
        start.sort()
        end.sort()
        
        rooms = 0
        
        left,right = 0,0
        
        """
                    l
        0    5    15
        10   20   30
                    r
        
        rooms = 2+
        
        """
        
        
        while left < length:
            if start[left] >= end[right]:
                rooms-=1
                right+=1
            rooms+=1
            left+=1
        return (rooms)