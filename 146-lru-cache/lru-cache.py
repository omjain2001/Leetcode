import heapq
from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.left = None
        self.right = None


# Using large space complexity
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

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.keys = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.right, self.tail.left = self.tail, self.head
    
    def removeNode(self, node):
        node.left.right, node.right.left = node.right, node.left
        node.left = node.right = None
    
    def insertNode(self, key, val):
        node = Node(key, val)
        node.left, node.right = self.head, self.head.right
        node.left.right = node.right.left = node
        return node

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        val = self.keys[key].val
        self.removeNode(self.keys[key])
        self.keys[key] = self.insertNode(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.removeNode(self.keys[key])
            del self.keys[key]
        
        if len(self.keys) == self.cap:
            del self.keys[self.tail.left.key]
            self.removeNode(self.tail.left)

        self.keys[key] = self.insertNode(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)