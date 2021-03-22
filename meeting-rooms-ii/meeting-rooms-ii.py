class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        length = len(intervals)
        
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])
        # print(start,end)
        
        sptr,eptr =0,0
        rooms = 0
        while sptr < length:
            if start[sptr] >= end[eptr]:
                rooms=rooms-1
                eptr = eptr+1
            
            rooms = rooms+1
            sptr = sptr+1
        
        return (rooms)
        
        