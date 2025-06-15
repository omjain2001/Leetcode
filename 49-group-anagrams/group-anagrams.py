class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            temp = "".join(sorted(word))
            if temp in hashmap:
                hashmap[temp].append(word)
            else:
                hashmap[temp] = [word]
        
        ans = list(hashmap.values())
        return ans
        