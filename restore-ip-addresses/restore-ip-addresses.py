class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not 4 <= len(s)<=12:
            return []
        
        def helper(idx,curr):
            nonlocal result
            #terminal condition
            if len(curr) ==4:
                if idx == len(s):
                    result.append('.'.join(curr))
                return
            #recursive condition
            num = ''
            for i in range(idx,min(idx+3,len(s))):
                num += s[i]
                #no leading zero 
                if num[0] == "0" and len(num)>1:
                    break
                
                # between zero and 255
                if 0 <= int(num)<=255:
                    curr.append(num)
                    helper(i+1,curr)
                    curr.pop()
                      
        result = []
        helper(0,[])
        return result
