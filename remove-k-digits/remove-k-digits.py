class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        temp = k
        stack = []
        for i in range(len(num)):
            while temp and stack and stack[-1] > num[i]:
            # if stack and stack[-1] > num[i] and k:
                stack.pop()
                temp = temp-1
            stack.append(num[i])
        res = "".join(stack[0:len(num)-k]).lstrip("0")
        if len(res):
            return res
        else:
            return "0"
            
        
        
        