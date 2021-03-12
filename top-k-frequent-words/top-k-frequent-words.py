class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dicti = {}
        res = []
        for i in words:
            if i in dicti:
                dicti[i] = dicti[i]+1
            else:
                dicti[i] = 1
        
        while len(res) < k:
            max_c = 0
            max_word = None
            
            for key,v in dicti.items():
                if v > max_c:
                    max_word =key
                    max_c = v
                    
                elif v == max_c and max_word > key:
                    max_word = key
                    max_c = v
                    
            res.append(max_word)
            dicti.pop(max_word)
        
        return res
            
                    
                    
        
              