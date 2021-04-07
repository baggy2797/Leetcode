class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        if len(sentence1)!=len(sentence2):
            return False
        
        if similarPairs:
            pairset = set(map(tuple,similarPairs))
            return all(w1==w2 or (w1,w2) in pairset or (w2,w1) in pairset for w1,w2 in zip(sentence1,sentence2))
                
        else:
            for i in range(len(sentence1)):
                if sentence1[i] != sentence2[i]:
                    return False
            return True
        
