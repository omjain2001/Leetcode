import heapq
from collections import defaultdict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(tuple)
        self.pq = []
        heapq.heapify(self.pq)
        self.time = 0

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.cache:
            self.cache[key] = (self.cache[key][0], self.time)
            heapq.heappush(self.pq, (self.time, key))
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        
        self.time += 1
        # Check capacity
        if (len(self.cache) == self.capacity) and key not in self.cache:
            # print('Working for key: ', key)
            while((len(self.pq) > 0) and (self.cache[self.pq[0][1]][1] > self.pq[0][0])):
                heapq.heappop(self.pq)

            # print(self.pq)
            t, recently_used_key = heapq.heappop(self.pq)
            del self.cache[recently_used_key]

        self.cache[key] = (value, self.time)
        heapq.heappush(self.pq, (self.time, key))



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)