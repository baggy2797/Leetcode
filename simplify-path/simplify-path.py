class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for element in path.split("/"):
            if element =="..":
                if stack:
                    stack.pop()
                    
            elif element == "." or not element:
                continue
                
            else:
                stack.append(element)
        
        res =  "/" + "/".join(stack)
        return res