from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count_map = defaultdict(int)
        order_set = set(list(order))

        others = ""

        for ch in s:
            if ch in order_set:
                count_map[ch] += 1
            else:
                others += ch

        print(count_map)
        print(others)

        result = ""

        for ch in order:
            if ch in count_map:
                result += (ch)*count_map[ch]
        
        result += others
        return result


        