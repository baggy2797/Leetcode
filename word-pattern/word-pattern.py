class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
    
        words = s.split(' ')
        pattern_dict = {}

        if len(pattern) != len(words):
            return False

        for p, w in zip(pattern, words):
            if p in pattern_dict:
                if pattern_dict[p] != w:
                    return False
            else:
                if w in pattern_dict.values():
                    return False
                pattern_dict[p] = w

        return True
            
        
        