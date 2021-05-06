class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        length = len(s)
        stack = []
        seen = set()
        freq = {c:i for i,c in enumerate(s)}
        
        for i,c in enumerate(s):
            if c not in seen:
        # for i in range(length):
        #     if stack and ord(stack[-1]) > ord(s[i]) and s[i] not in stack:
                while stack and ord(stack[-1]) > ord(c) and i < freq[stack[-1]]:
                    seen.discard(stack.pop())
                    # stack.pop()
                seen.add(c)

                stack.append(c)
            # elif s[i] in stack:continue
            # else: stack.append(s[i])
        return "".join(stack)
                
        
        
        