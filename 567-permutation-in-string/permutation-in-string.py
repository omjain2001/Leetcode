class Solution:    
    def compare_lists(self, l1, l2):
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        return True


    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False
        
        list1 = [0] * 26
        list2 = [0] * 26


        for ch in s1:
            list1[ord(ch)-ord('a')] += 1
            
        l = 0
        r = 0
        while(r < len(s2)):
            if (r-l+1) > len(s1):
                ch_idx = ord(s2[l]) - ord('a')
                list2[ch_idx] -= 1
                l += 1
            ch_idx = ord(s2[r]) - ord('a')
            list2[ch_idx] += 1
            # print(f"{s2[r]}: {list2}")
            if self.compare_lists(list1, list2):
                return True  
            r += 1
        
        return False        