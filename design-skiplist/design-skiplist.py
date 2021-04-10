class Skiplist:

    def __init__(self):
        self.freq = {}  

    def search(self, target: int) -> bool:
        if target in self.freq and self.freq[target]>0:
            return True
        return False

    def add(self, num: int) -> None:
        if num in self.freq:
            self.freq[num]+=1
        else:
            self.freq[num]=1
            
    def erase(self, num: int) -> bool:
        if num in self.freq and self.freq[num]!=0:
            self.freq[num]-=1
            return True
        return False


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)