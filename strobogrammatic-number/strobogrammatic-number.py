class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        sample = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        
        res = []
        
        for c in reversed(num):
            if c not in sample:
                return False
            res.append(sample[c])
        
        rot_s = "".join(res)
        return rot_s == num