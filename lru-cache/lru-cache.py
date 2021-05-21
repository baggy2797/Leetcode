

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity  
        self.cache = {}
        
    def get(self, key: int) -> int:
        value = self.cache.get(key,None)
        if value is not None:
            del self.cache[key]
            self.cache[key] = value
            return value
        else:return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        else:
            if (len(self.cache)) == self.capacity:
                del self.cache[next(iter(self.cache))]
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)