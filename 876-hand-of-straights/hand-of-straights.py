from collections import defaultdict
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # Check if the numbers can be grouped in groupSize
        if (len(hand) % groupSize) != 0:
            return False
        hashMap = defaultdict(int)
        
        for num in hand:
            hashMap[num] += 1
        
        minHeap = list(hashMap.keys())
        heapq.heapify(minHeap)
        
        while(len(minHeap) > 0):
            mini = minHeap[0]
            # if hashMap[mini] == 0:
            #     heapq.heappop(minHeap)
            #     continue
            
            for i in range(groupSize):
                if (mini+i) in hashMap:
                    hashMap[mini+i] -= 1
                    if hashMap[mini+i] == 0:
                        if (mini+i) != minHeap[0]:
                            return False
                        heapq.heappop(minHeap)
                else:
                    return False
        return True        