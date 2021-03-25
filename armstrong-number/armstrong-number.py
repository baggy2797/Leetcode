class Solution:
    def isArmstrong(self, n: int) -> bool:
        if n <=9:
            return n
        armstrongNum = 0
        n = str(n)
        power = len(n)
        for i in range(len(n)):
            armstrongNum = armstrongNum + ( (int(n[i]))**power )
        
        return (armstrongNum == int(n))
        