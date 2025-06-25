class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = r = 0
        length = 0
        for r in range(len(s)):
            if s[r] in charset:
                while l < r and s[l] != s[r]:
                    charset.remove(s[l])
                    l += 1
                charset.remove(s[r])
                l += 1
            charset.add(s[r])
            length = max(length, len(charset))

        return length
            

        