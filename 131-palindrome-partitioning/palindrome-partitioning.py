class Solution:
    def isPalindrome(self, s, start, end):
        while(start <= end):
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def recur(self, s, idx, temp, ans):
        if idx == len(s):
            ans.append(temp.copy())
            return
        
        for i in range(idx, len(s)):
            if self.isPalindrome(s, idx, i):
                temp.append(s[idx: i+1])
                self.recur(s, i+1, temp, ans)
                temp.pop()
        
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.recur(s, 0, [], ans)
        return ans
        