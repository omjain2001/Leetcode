class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:
                while(len(stack) > 0 and stack[-1] > 0 and stack[-1] < abs(i)):
                    stack.pop()
                if len(stack) > 0 and stack[-1] > 0:
                    if stack[-1] == abs(i):
                        stack.pop()
                else:
                    stack.append(i)
                
                        
        return stack
        