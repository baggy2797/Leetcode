class RandomizedSet:
    #Every function must operate in O(1) runtime
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = []
        self.fetcher = {}
        self.length = 0
        
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.fetcher:return False
        self.storage.append(val)
        self.fetcher[val] = self.length
        self.length+=1
        return True
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.fetcher:return False
        #swap the last and the required element
        lastElement = self.storage[self.length-1]
        val_idx = self.fetcher[val]
        
        self.storage[val_idx],self.storage[self.length-1] = self.storage[self.length-1],self.storage[val_idx]
        self.fetcher[lastElement] = val_idx
        del self.fetcher[self.storage[self.length-1]]
        self.length-=1
        self.storage.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.storage)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()