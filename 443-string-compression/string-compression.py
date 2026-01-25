class Solution:
    def compress(self, chars: List[str]) -> int:

        if len(chars) == 0:
            return 0

        prev = chars[0]
        count = 1
        j = 0
        i = 1
        while(i < len(chars)):
            if chars[i] == prev:
                count += 1
            else:
                chars[j] = prev
                j += 1
                temp = ""
                if count > 1:
                    while(count):
                        temp += str(count%10)
                        count = count // 10
                    for k in range(len(temp)-1, -1, -1):
                        chars[j] = temp[k]
                        j += 1

                prev = chars[i]
                count = 1
            i += 1
        
        # Add the last segment
        chars[j] = prev
        j += 1
        if count > 1:
            temp = ""
            while(count):
                temp += str(count%10)
                count = count // 10
            for k in range(len(temp)-1, -1, -1):
                chars[j] = temp[k]
                j += 1
        
        return j
                
        