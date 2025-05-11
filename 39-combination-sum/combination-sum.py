class Solution:
    def recur(self, idx, candidates, target, comb, ans):
        if target == 0:
            ans.append(comb.copy())
            return
        if idx == 0:
            if target % candidates[idx] == 0:
                comb += [candidates[idx]]*(target//candidates[idx])
                ans.append(comb)
            return
        
        if target >= candidates[idx]:
            self.recur(idx, candidates, target-candidates[idx], comb + [candidates[idx]], ans)
        
        self.recur(idx-1, candidates, target, comb, ans)
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.recur(len(candidates)-1, candidates, target, [], ans)
        return ans
        