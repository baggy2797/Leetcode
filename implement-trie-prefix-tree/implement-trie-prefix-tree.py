class TrieNode:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.end = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        parent = self.root
        for i,char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TrieNode(char)
            parent = parent.children[char]
            
            if i == len(word)-1:
                parent.end = True
                
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return parent.end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)