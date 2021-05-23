class LRUCache:

    def __init__(self, capacity: int):
        self.storage = OrderedDict()        
        self.capacity = capacity
        self.length = 0
    def get(self, key: int) -> int:
        val = self.storage.get(key,-1)
        if val!=-1:
            del self.storage[key]
            self.storage[key] = val
        return val
    
    def put(self, key: int, value: int) -> None:
        if key in self.storage.keys():
            del self.storage[key]
            self.storage[key] = value
        else:
            if len(self.storage) == self.capacity:
                self.storage.popitem(last=False)
            self.storage[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)