class Solution:
    def exhaustive_search(self, idx, candidates, target, ans, comb):
        if target == 0:
            ans.append(comb)
            return
        if idx == len(candidates):
            return
        
        # Take
        if target >= candidates[idx]:
            self.exhaustive_search(idx+1, candidates, target-candidates[idx], ans, comb + [candidates[idx]])
        
        while(idx+1 < len(candidates) and candidates[idx+1] == candidates[idx]):
            idx += 1
        # Don't take
        self.exhaustive_search(idx+1, candidates, target, ans, comb)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.exhaustive_search(0, candidates, target, ans, [])
        return ans
        