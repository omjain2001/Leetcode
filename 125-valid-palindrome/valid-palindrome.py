class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while(i <= j):
            if not (s[i].isdigit() or s[i].isalpha()):
                i += 1
            elif not (s[j].isdigit() or s[j].isalpha()):
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1

        return True
                
        