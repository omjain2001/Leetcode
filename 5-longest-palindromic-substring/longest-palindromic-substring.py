class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_count = 1
        start = 0
        end = 0
        
        for i in range(len(s)):

            # Odd palindrome
            j = i-1
            k = i+1

            while(j >= 0 and k < len(s)):
                if s[j] != s[k]:
                    break
                j -= 1
                k += 1
            
            if (k-j-1) > max_count:
                max_count = max(max_count, (k-j-1))
                start = j+1
                end = k-1

            # Even palindrome
            j = i
            k = i+1

            while(j >= 0 and k < len(s)):
                if s[j] != s[k]:
                    break
                j -= 1
                k += 1
            
            if (k-j-1) > max_count:
                max_count = max(max_count, (k-j-1))
                start = j+1
                end = k-1
        
        return s[start:end+1]
        