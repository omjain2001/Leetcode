class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if k == 0:
            return 0

        hashmap = {}
        max_substr = 0
        l = 0
        r = 0
        while(r < len(s)):
            hashmap[s[r]] = r
            if len(hashmap) > k:
                while(l <= r and len(hashmap) > k):
                    if hashmap[s[l]] == l:
                        hashmap.pop(s[l])
                    l += 1
            
            max_substr = max(max_substr, r-l+1)
            r += 1
        
        return max_substr