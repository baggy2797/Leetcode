class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransomNote_dict,magazine_dict = Counter(ransomNote),Counter(magazine)
        
        for ch in ransomNote:
            if ransomNote_dict.get(ch) is None or magazine_dict.get(ch) is None:return False
            if ransomNote_dict.get(ch) <= magazine_dict.get(ch):
                continue
            else:
                return False
        return True
            
        
        