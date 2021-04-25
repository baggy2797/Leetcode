class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        freq = {x:i for i,x in enumerate(B)}
        
        return [freq[x] for x in A]
        