class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        freq = collections.Counter()
        
        length = len(s)
        for i in range(length - minSize + 1):
            t = s[i : i+minSize]
            if len(set(t)) <= maxLetters:
                freq[t] += 1
        
        return max(freq.values()) if freq else 0
#         length = len(s)
#         store = {}
#         freq = {}
#         left,right = 0,0
        
#         while right <length:
#             windowSize = right - left+1
            
#             if windowSize < minSize:
#                 freq[s[right]] = freq.get(s[right],0)+1
#                 right+=1
            
#             elif windowSize > maxSize:
#                 freq[s[left]] = freq.get(s[left],0)-1
#                 if freq[s[left]] == 0: del freq[s[left]]
#                 left+=1
        
#             elif minSize <= windowSize <= maxSize: 
#                 if len(freq)<= maxLetters:
#                     store[s[left:right+1]] = store.get(s[left:right+1],0)+1
#                     left+=1
#                 right+=1
#         print(store)
#         return max(store.values()) 
                
#         length = len(s)
#         freq = {}
#         unique = 0
#         left,right = 0,0
#         hash = {}
#         flag = 0
#         while right < length:
#             freq[s[right]] = freq.get(s[right],0) + 1
#             unique +=1 if freq[s[right]] == 1 else 0
            
#             currWindowSize = (right-left+1)
            
#             if unique <= maxLetters:
#                 if minSize <= currWindowSize <= maxSize:
#                     subs = (s[left:right+1])
#                     # print(subs,left,right,hash.get(subs,0))
#                     hash[subs] = hash.get(subs,0)+1
#                     #left+=1
                
#             else:
#                 if s[left] in freq:
#                     freq[s[left]] = 1
#                     if freq[s[left]] == 0:
#                         del freq[s[left]]
#                         unique-=1
#                 # left+=1
#                     flag = 1
#             if flag: 
#                 left+=1
#                 flag = 0
#             else: right+=1
                
#             # right+=1
#         return max(hash.values())