class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        c3,c5 = 0,0
        for i in range(1,n+1):
            d = ""
            c3 = c3+1
            c5 = c5+1
            if c3 == 3:
                d += "Fizz"
                c3 = 0
            if c5 == 5:
                d += "Buzz"
                c5 = 0
            res.append(d or str(i))
        
        return res
                