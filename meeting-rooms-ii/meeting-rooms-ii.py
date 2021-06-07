class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        0  5  15
        10 20 30
        
        2 
        
        """
        if not intervals:return 0
        length = len(intervals)
        intervals.sort()
        startTimings = []
        endTimings = []
        
        for interval in intervals:
            startTimings.append(interval[0])
            endTimings.append(interval[1])
        endTimings.sort()
        
        left = 0 
        right = 0
        rooms = 0
        while left < length:
            if startTimings[left] >= endTimings[right]:
                rooms-=1
                right+=1
            
            rooms+=1
            left+=1
        return (rooms)