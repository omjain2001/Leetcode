class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hashmap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        ans = []
        for d in digits:
            temp = []
            for ch in hashmap[d]:
                if len(ans) > 0:
                    for i in ans:
                        temp.append(i + ch)
                else:
                    temp.append(ch)
            
            ans = temp.copy()
            temp = []
        
        return ans
            
        