class Solution:
    def compare_lists(self, s_list, t_list):
        for i in range(128):
            if t_list[i] > 0 and s_list[i] < t_list[i]:
                return False
        return True


    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        list1 = [0] * 128
        list2 = [0] * 128

        for ch in t:
            idx = ord(ch) - ord('A')
            list2[idx] += 1
        
        l = 0
        r = 0

        mini = 1e10
        start = end = -1

        while(r < len(s)):
            
            idx = ord(s[r]) - ord('A')
            list1[idx] += 1
            
            while (l <= r and self.compare_lists(list1, list2)):
                if (r-l+1) < mini:
                    mini = r-l+1
                    start = l
                    end = r
                idx = ord(s[l]) - ord('A')
                list1[idx] -= 1
                l += 1
            
            r += 1
        
        while (l < r and self.compare_lists(list1, list2)):
            if (r-l+1) < mini:
                mini = r-l+1
                start = l
                end = r
            idx = ord(s[l]) - ord('A')
            list1[idx] -= 1
            l += 1
        
        if start == -1:
            return ""
        return s[start:end+1]
        