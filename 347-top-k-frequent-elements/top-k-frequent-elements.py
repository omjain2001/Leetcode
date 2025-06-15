from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = defaultdict(int)
        for ele in nums:
            hashmap[ele] += 1
        
        q = []
        heapq.heapify(q)
        for key, val in hashmap.items():
            heapq.heappush(q, (-val, key))
        
        ans = []
        while(k):
            ans.append(heapq.heappop(q)[1])
            k -= 1
        return ans
        
        