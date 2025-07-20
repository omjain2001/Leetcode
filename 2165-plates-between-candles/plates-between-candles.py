class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        plate_prefix = [0] * len(s)
        candle_prefix = [0] * len(s)
        candle_suffix = [0] * len(s)

        pp = 0
        for i in range(len(s)):
            if s[i] == '*':
                plate_prefix[i] = pp + 1
                pp += 1
            else:
                plate_prefix[i] = pp
        
        candle_prefix[0] = 0 if s[0] == '|' else -1
        candle_suffix[len(s)-1] = len(s)-1 if s[len(s)-1] == '|' else len(s)

        for i in range(1, len(s)):
            if s[i] == '|':
                candle_prefix[i] = i
            else:
                candle_prefix[i] = candle_prefix[i-1]
        
        for i in range(len(s)-2, -1, -1):
            if s[i] == '|':
                candle_suffix[i] = i
            else:
                candle_suffix[i] = candle_suffix[i+1]

        result = []
        
        for q in queries:
            st, e = q
            if s[st] == '*':
                st = candle_suffix[st]
            if s[e] == '*':
                e = candle_prefix[e]
            
            if st >= e:
                result.append(0)
            else:
                result.append(plate_prefix[e]-plate_prefix[st])
            
        return result
        