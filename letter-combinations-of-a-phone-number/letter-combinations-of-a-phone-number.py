class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        res = []
        for digit in digits:
            newRes = []
            if res:
                holder = res
                for i in range(len(mapping[digit])):
                    for val in holder:
                        new = ""
                        new += val + mapping[digit][i]
                        
                        newRes.append(new)
                res = newRes
            else:
                for val in mapping[digit]:
                    res.append(val)
        
        return res
        
        
                
                
    