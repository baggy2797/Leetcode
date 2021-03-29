class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_of_alphabets={}
        for i in range(len(order)):
            order_of_alphabets[order[i]]=i
            
        for i in range(len(words)-1):
            for j in range(min(len(words[i]),len(words[i+1]))):
                if order_of_alphabets[words[i][j]]<order_of_alphabets[words[i+1][j]]:
                    break
                elif order_of_alphabets[words[i][j]]>order_of_alphabets[words[i+1][j]]:
                    return False
            else:
                if len(words[i])>len(words[i+1]):
                    return False
        return True
            