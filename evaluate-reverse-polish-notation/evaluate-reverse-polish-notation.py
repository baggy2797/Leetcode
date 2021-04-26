class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # operators = {"+","-","*","/"}
        for token in tokens:
            if token[-1].isdigit():
                stack.append(int(token))
            # elif token in operators:
            else:
                second = stack.pop() 
                first = stack.pop()
                
                if token == "+": 
                    stack.append(first + second)
                elif token == "-": 
                    stack.append(first - second)
                elif token == "*": 
                    stack.append(first * second)
                else: 
                    stack.append(int(float(first) / second))
        
        return stack.pop()                