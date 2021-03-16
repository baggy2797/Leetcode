class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        length = len(s)
        res = ""
        while i < length:
            if s[i] == "#":
                temp = ""
                temp = int(s[i-2:i])
                temp = temp + ord('a') -1
                res = res + chr(temp)
                if (i+3)<length and s[i+3]== "#":
                    i = i+3
                else:
                    i = i+1
            elif (i+2)<length and s[i+2]=='#':
                i+=2
            else:
                temp = ""
                temp = int(s[i])
                if temp == 0:
                    temp = ord('a')
                else:
                    temp = temp + ord('a')-1
                res = res + chr(temp) 
                i = i+1
            # else:
            #     continue
        return res