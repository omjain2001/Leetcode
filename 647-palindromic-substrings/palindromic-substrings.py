class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            total += 1

            # Odd palindrome
            j = i-1
            k = i+1

            while(j >= 0 and k < len(s)):
                if s[j] != s[k]:
                    break
                total += 1
                j -= 1
                k += 1

            # Even palindrome
            j = i
            k = i+1

            while(j >= 0 and k < len(s)):
                if s[j] != s[k]:
                    break
                total += 1
                j -= 1
                k += 1
        
        return total


        