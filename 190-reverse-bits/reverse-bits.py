class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 0
        num = n
        count = 32
        while(count):
            if num & 1:
                mask += 1
            if count == 1:
                break
            mask = mask << 1
            num = num >> 1
            count -= 1
        return mask

        

        