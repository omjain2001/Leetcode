from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        if len(strings) == 0:
            return []

        # For each element, calculate the distance between all letters. Generate a unique key out of it

        hashmap = defaultdict(list)

        for word in strings:
            if len(word) == 0:
                continue
            key = str(len(word)) + '$'
            for ch in range(1,len(word)):
                if word[ch-1] <= word[ch]:
                    key += str(ord(word[ch])-ord(word[ch-1]))
                else:
                    key += str(26-(ord(word[ch-1])-ord(word[ch])))
                key += '$'
            hashmap[key].append(word)
        
        return list(hashmap.values())

        