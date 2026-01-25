# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        # # Brute force
        # celebrity = -1
        # for i in range(n):
        #     is_celebrity = True
        #     for j in range(n):
        #         if j != i and not knows(j,i):
        #             is_celebrity = False
        #             break
            
        #     if is_celebrity:
        #         celebrity = i
        #         break

        # ## Verify if the celebrity does not know anyone
        # if celebrity == -1:
        #     return -1
        # else:
        #     for i in range(n):
        #         if i != celebrity and knows(celebrity,i):
        #             return -1
        
        # return celebrity

        # Better approach
        celebrity = 0
        for i in range(1,n):
            if not knows(i,celebrity):
                # Since i knows celebrity, i is not a celebrity. Else, i can be a celebrity
                celebrity = i
        
        for i in range(n):
            if i != celebrity and (knows(celebrity, i) or not knows(i,celebrity)):
                return -1
        return celebrity
        