class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        hashmap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        temp = []
        for d in digits:
            for i in hashmap[d]:
                if len(ans) > 0:
                    for j in ans:
                        temp.append(j + i)
                else:
                    temp.append(i)
            ans = temp.copy()
            temp = []
        return ans
        
        