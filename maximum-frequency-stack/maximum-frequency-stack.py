class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = {}
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] = self.freq.get(val,0)+1

    def pop(self) -> int:
        maxVal = max(self.freq.values()) #O(n)
        
        temp = []
        
        #find the key closest to the top
        for i in range(len(self.stack)-1,-1,-1):
            if self.freq[self.stack[i]] == maxVal:
                temp.append((self.stack[i],i))
                break
        # print(i)
        
        
        
        miniKey = 0
        mini = len(self.stack)
        for key,idx in temp:
            if idx <= mini:
                mini = idx
                miniKey = key
        
        
        self.freq[miniKey]-=1
        # print(self.stack,self.freq)
        return self.stack.pop(idx)
            
    
                
        
            
        
    

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()