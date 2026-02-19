class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []
        temp = []

        def is_palindrome(i, j):
            while(i <= j and s[i] == s[j]):
                i += 1
                j -= 1
            if i <= j:
                return False
            return True

        def recur(i):
            if i == len(s):
                result.append([ele for ele in temp])
                return
            
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    temp.append(s[i:j+1])
                    recur(j+1)
                    temp.pop()
        
        recur(0)
        return result

        