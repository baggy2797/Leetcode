class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(res,curr,left,right):
            if left<0 or left>right:
                return
            if left==0 and right ==0:
                res.append(curr)
                return
            
            helper(res,curr+"(",left-1,right)
            helper(res,curr+")",left,right-1)
        
        
        helper(res,"",n,n)
        return res
    
        

        # r = ["()"]
        # for _ in range(n-1):
        #     r = [i[0:j+1]+"()"+i[j+1:] for i in r for j in range(len(i))]
        #     r = list(dict.fromkeys(r))
        # return r
        