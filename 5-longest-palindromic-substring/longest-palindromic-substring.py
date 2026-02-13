class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Define function to compute length of palindrome
        def palindrome_length(l, r):
            length = 0
            start = -1
            end = -1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if (r-l+1) > length:
                    length = r-l+1
                    start = l
                    end = r
                    l -= 1
                    r += 1
            return length, (start, end)
        

        maxi = 0
        start = -1
        end = -1
        i = 0

        while(i < len(s)):
            # Check for odd palindrome
            length, pos = palindrome_length(i, i)
            if length > maxi:
                maxi = length
                start = pos[0]
                end = pos[1]

            # Check for even palindrome
            length, pos = palindrome_length(i, i+1)
            if length > maxi:
                maxi = length
                start = pos[0]
                end = pos[1]

            i += 1
        
        if maxi == 0:
            return ""
        return s[start:end+1]        