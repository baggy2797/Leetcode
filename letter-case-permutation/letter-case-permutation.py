class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        # print(S)
        
        res = []
        for i in range(len(S)):
            
            #work on digits
            if S[i].isdigit():
                if res:
                    for r in range(len(res)):
                        res[r] = res[r] + str(S[i])
                else:
                    res.append(S[i])
                
            elif S[i].isalpha():
                #work on alphabets
                if res:
                    temp = res.copy()
                    res = []
                    for r in range(len(temp)):
                        upper = temp[r]+ S[i].upper()
                        lower = temp[r] + S[i].lower()
                        res.append(lower)
                        res.append(upper)

                else:
                    res.append(S[i].upper())
                    res.append(S[i].lower())
                
                # print(S[i])
        
        return res
        # new = ""
        # res = []
        # for i in range(len(S)):
        #     if S[i].isdigit():
        #         if res:
        #             for sub in range(len(res)):
        #                 res[sub]=res[sub]+S[i]
        #         else:
        #             res.append(S[i])
        #     if S[i].isalpha():
        #         if not res:
        #             res.append(S[i].lower())
        #             res.append(S[i].upper())
        #         elif res:
        #             lower,upper = res.copy(),res.copy()
        #             for k in range(len(lower)):
        #                 lower[k]+=S[i].lower()
        #             for p in range(len(upper)):
        #                 upper[p]+=S[i].upper()
        #             print(upper,lower)
        #             res = []
        #             res = upper+lower
        # return res            