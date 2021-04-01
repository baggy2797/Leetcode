class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        new = ""
        res = []
        for i in range(len(S)):
            if S[i].isdigit():
                if res:
                    for sub in range(len(res)):
                        res[sub]=res[sub]+S[i]
                else:
                    res.append(S[i])
            if S[i].isalpha():
                if not res:
                    res.append(S[i].lower())
                    res.append(S[i].upper())
                elif res:
                    lower,upper = res.copy(),res.copy()
                    for k in range(len(lower)):
                        lower[k]+=S[i].lower()
                    for p in range(len(upper)):
                        upper[p]+=S[i].upper()
                    print(upper,lower)
                    res = []
                    res = upper+lower
        return res
                
                
                
#             else:
#                 temp = []
#                 temp.append(S[i])
#                 upper,lower = S[i].upper(),S[i].lower()
                
#                 x =""
#                 for n in res:
#                     upper = n+upper
#                     lower = n+lower
                
#                 print(lower,upper)
                    
#         print(res)
            