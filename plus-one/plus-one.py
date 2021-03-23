class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = [str(integer) for integer in digits]
        a_string = "".join(strings)
        num = int(a_string)
        num = num + 1
        
        return [int(i) for i in str(num)]