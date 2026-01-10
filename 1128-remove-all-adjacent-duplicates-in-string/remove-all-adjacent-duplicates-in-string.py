class Solution:
    def removeDuplicates(self, s: str) -> str:
        new_str = ""
        for ele in s:
            if len(new_str) > 0 and new_str[-1] == ele:
                new_str = new_str[:-1]
            else:
                new_str = new_str + ele
        return new_str
        