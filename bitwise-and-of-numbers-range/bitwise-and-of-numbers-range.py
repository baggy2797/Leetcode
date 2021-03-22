class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        temp = 0
        while right > left:
                right = right&(right-1)
        return right&left
        