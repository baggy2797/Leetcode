class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        length = len(s)
        opens ,closes = [],[]
        
        for i in range(length):
            if s[i] == "(":
                opens.append(i)
            elif s[i] == ")":
                if opens:
                    opens.pop()
                else:
                    closes.append(i)
        
        temp = set(opens+closes)
        
        return ''.join(s[i] for i in range(length) if i not in temp)
        
        