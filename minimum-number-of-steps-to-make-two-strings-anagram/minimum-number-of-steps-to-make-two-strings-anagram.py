class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c_s = Counter(s)
        count = 0
        # print(c_s)
        for i in t:
            # print(i)
            if c_s[i] is None or c_s[i] == 0:
                count+=1
            else:
                c_s[i]-=1
                continue
        return (count)
        
        