class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.hashMap = {}
        self.length = 0
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hashMap:return False
        self.array.append(val)
        self.hashMap[val] = self.length
        self.length+=1
        return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hashMap:return False
        if val == self.array[-1]:
            del self.hashMap[val]
            self.array.pop()
        else:
            lastElement,lastElementIdx = self.array[-1],self.length-1
            val_idx = self.hashMap[val]
            
            # print(self.array,self.hashMap)
            self.array[val_idx],self.array[lastElementIdx] = self.array[lastElementIdx],self.array[val_idx]
            self.hashMap[lastElement] = val_idx
            self.array.pop()
            del self.hashMap[val]
        self.length-=1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()