class TrieNode:
    def __init__(self,val):
        self.val =val
        self.children = {}
        self.endhere = False
    
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def addWord(self, word: str) -> None:
        parent = self.root
        for idx,char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TrieNode(char)
            parent = parent.children[char]
            
            if idx == len(word) - 1:
                parent.endhere = True
        

    def search(self, word: str) -> bool:
        parent = self.root
        def searchWord(word,parent):
            for idx,char in enumerate(word):
                if char not in parent.children:
                    if char == ".":
                        for each in parent.children:
                            if searchWord(word[idx+1:],parent.children[each]):
                                return True
                    return False
                parent = parent.children[char]
            return parent.endhere
        
        return searchWord(word,parent)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)