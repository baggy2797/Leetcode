class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        length = len(asteroids)
        stack = []
        for i in range(length):
            while stack and asteroids[i] < 0 < stack[-1]:
                if stack[-1] < (-1)* asteroids[i]:
                    stack.pop()
                    continue
                    # stack.append(asteroids[i])
                elif stack[-1] == (-1)*asteroids[i]:
                    stack.pop()
                break
            else:
                stack.append(asteroids[i])
        return (stack)
            