from collections import deque
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # Length of candidates
        n = len(candidates)
        ans = deque()

        if n == 0:
            return []

        # Sort the candidates
        candidates.sort()

        result = set()

        def recur(i, s):
            if (s == 0): 
                result.add(tuple([ele for ele in ans]))
                return
            if (i >= n or s < 0 or candidates[i] > s):
                return
            
            # Take
            ans.append(candidates[i])
            recur(i+1, s-candidates[i])
            ans.pop()

            while((i+1) < n and candidates[i+1] == candidates[i]):
                i += 1
            recur(i+1, s)

        recur(0,target)
        
        final_ans = []
        for ele in result:
            final_ans.append(list(ele))
        
        return final_ans
        

        