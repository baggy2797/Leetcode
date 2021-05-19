class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        record = defaultdict(int)
        res = 0
        length = len(s)
        for i in range(length - minSize + 1):
            substring = s[i:i+minSize]
            if len(set(substring))<= maxLetters:
                record[substring]+=1
                res = max(res,record[substring])
        return res
        
#         length = len(s)
#         left = 0
#         right = 0
#         windowSize = minSize
#         temp = {}
        
#         while right< length:
#             if right-left < minSize:right+=1            
#             if right-left >=minSize:left+=1
#             if len(set(Counter(s[left:right+1])))<= maxLetters:
#                 temp[(s[left:right+1])] = temp.get((s[left:right+1]),0)+1
#         print(temp)
#         maxValue = 0
#         for key,value in temp.items():
#             if value > maxValue:
#                 maxValue = value
    
#         return maxValue
            
        