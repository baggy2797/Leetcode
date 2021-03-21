class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        res= []
        while len(n)!='1' and n not in res:
            res.append(n)
            temp = 0
            for nm in n:
                
                temp = temp + int(nm) *(int(nm))
            # print(temp)
            n = str(temp)
        
        if int(n) == 1:
            return True
        return False
        
        