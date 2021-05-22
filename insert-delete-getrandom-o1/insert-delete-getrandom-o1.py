class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = []
        self.fetching = {}
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.fetching:return False
        self.fetching[val] = len(self.store)
        self.store.append(val)
        return True

    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.fetching:return False
        
        lastElement,val_idx = self.store[-1],self.fetching[val]
        self.store[val_idx] = lastElement
        self.fetching[lastElement] = val_idx
        self.store.pop()
        del self.fetching[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.store)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()