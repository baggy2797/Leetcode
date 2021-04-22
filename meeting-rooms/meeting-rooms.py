class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        print(intervals)
        for i in range(1,len(intervals)):
            start1,end1 = (intervals[i-1])
            start2,end2 = (intervals[i])
            # print(start1,end1,start2,end2)
            if start1 == start2:
                return False
            elif end1 > start2:
                return False
            else:
                continue
            
        return True