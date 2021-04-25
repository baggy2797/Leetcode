class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        
        else:
            stack_min = self.stack[-1][1]
            if val < stack_min: 
                self.stack.append((val,val))
            else:
                self.stack.append((val,stack_min))
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]

        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()