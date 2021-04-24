class Solution:
    def reverseBits(self, n: int) -> int:
        # print(len(str(n)))
        ret,power = 0,31
        while n:
            ret+=(n&1) << power
            # print(ret)
            n = n>>1
            power-=1
        return ret
        
        