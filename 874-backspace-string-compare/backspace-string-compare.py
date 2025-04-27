class Solution:
    def get_valid_string(self, s):
        ans = ""
        for i in s:
            if i == '#':
                ans = ans[:-1]
            else:
                ans = ans + i
        return ans

    def backspaceCompare(self, s: str, t: str) -> bool:
        s_new = self.get_valid_string(s)
        t_new = self.get_valid_string(t)

        print(s_new, t_new)

        return (s_new == t_new)
        
        