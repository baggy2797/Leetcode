class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        res =[]
        for time in timePoints:
            time = time.split(":")
            res.append(int(time[0])*60+int(time[1]))
            res.append(24*60+int(time[1])+int(time[0])*60)
        print(res)
        res.sort()
        ans = float('inf')
        
        for i in range(len(res)-1):
            ans = min(ans,res[i+1]-res[i])
        return (ans)