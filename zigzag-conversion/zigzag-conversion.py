class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 0 or len(s) == 1 or numRows ==1:
            return s
        
        
        rows = [""]*numRows
        
        flag = False
        i = 0
        for char in s:
            rows[i] = "".join([rows[i],char])
            if i == 0 or i == numRows-1:
                flag = not flag
            if flag:
                i=i+1
            else:
                i=i-1
        
        return "".join(rows)
               