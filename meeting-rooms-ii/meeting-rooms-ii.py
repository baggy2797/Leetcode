class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:return 0
        length = len(intervals)
        startTimings = [0 for _ in range(length)]
        endTimings = [0 for _ in range(length)]
        
        for i in range(length):
            startTimings[i] = (intervals[i][0])
            endTimings[i] = (intervals[i][1])
        
        startTimings.sort()
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