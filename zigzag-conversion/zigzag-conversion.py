class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)

        if numRows == 1:
            return s
        elif numRows == 2:
            return s[0:length:2]+s[1:length:2]
        else:
            res = [[0 for _ in range(length)] for _ in range(numRows)]
            rows,cols=len(res),len(res[0])

            r,c = 0,0
            i = 0

            flag = 0 # 0 meand go down and 1 means go up diagonally 
            #Go Down Columnwise
            #column is constant increase the r
            while i < length:
                res[r][c] = s[i]
                if flag == 0:
                    if r == rows-1:
                        r-=1
                        c+=1
                        flag = 1
                    else:
                        r+=1
                else:
                    if r == 0:
                        flag = 0
                        r+=1
                    else:
                        r-=1
                        c+=1
                i+=1

            new = ""
            # print(res)
            for j in range(numRows):
                for k in range(length):
                    if res[j][k] != 0:
                        new +=(res[j][k])
            return (new)
                    
                    
        
            
            