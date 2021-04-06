class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        m1 = m2 = m3 =True
        # if first letter is uppercase
        
        if word[0].isupper():
            temp = []
            #if all words are uppercase
            for i in range(1,len(word)):
                if not word[i].isupper():
                    m1 = False
                    break
            if m1:
                return True
            
            for i in range(1,len(word)):
                if word[i].isupper():
                    m2 = False
                    break
            if m2:
                return True
        else:
            #if all words are lowercase
            check = word.lower()
            if check == word:
                return True