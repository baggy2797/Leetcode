class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rota = rotb = 0
            for i in range(n):
                if tops[i] != x and bottoms[i]!=x:
                    return -1
                elif tops[i]!=x:
                    rota+=1
                elif bottoms[i]!=x:
                    rotb+=1
            return min(rota,rotb)
        
        n = len(tops)
        rotations = check(tops[0])
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        else: return check(bottoms[0])