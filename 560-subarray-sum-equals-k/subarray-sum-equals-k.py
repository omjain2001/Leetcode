class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        hashmap[0] = 1
        count = 0
        sum = 0

        for i in nums:
            sum += i
            if (sum - k) in hashmap:
                count += hashmap[sum - k]
            hashmap[sum] = hashmap.get(sum, 0) + 1

        return count