class Bucket:
    def __init__(self):
        self.bucket = []
        
    def getVal(self,key):
        for (k,v) in (self.bucket):
            if k == key:
                return v
        return -1
        
    def update(self,key,value):
        found = False
        for i,kv in enumerate(self.bucket):
            if kv[0] == key:
                found = True
                self.bucket[i] = (key,value)
                break
        if not found:
            self.bucket.append((key,value))
            
    def remove(self,key):
        for i,kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
            
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashValue = 2069
        self.Map = [Bucket() for i in range(self.hashValue)]


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashKey = key % self.hashValue
        self.Map[hashKey].update(key,value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        
        hashKey = key % self.hashValue
        # print(self.Map[hashKey].bucket)
        return self.Map[hashKey].getVal(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashKey = key % self.hashValue
        self.Map[hashKey].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)