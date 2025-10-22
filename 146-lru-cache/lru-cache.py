class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # Store capacity
        self.capacity = capacity
        
        # Create dummy head and tail
        self.head = Node(None, None)
        self.tail = Node(None, None)

        # Connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

        # Create a hashmap
        self.hashmap = {}

    
    def insert_node(self, key, val):
        newnode = Node(key, val)
        newnode.prev = self.head
        newnode.next = self.head.next
        self.head.next.prev = newnode
        self.head.next = newnode

        self.hashmap[key] = newnode
    

    def remove_node(self, key):
        deprecated_node = self.hashmap[key]
        deprecated_node.prev.next = deprecated_node.next
        deprecated_node.next.prev = deprecated_node.prev

        self.hashmap.pop(key)

        deprecated_node = None


    def get(self, key: int) -> int:

        # Check if the value is present in the cache
        if key in self.hashmap:

            # Store the value
            val = self.hashmap[key].val
            
            # Remove the key from the cache
            self.remove_node(key)

            # Insert the key as in the cache
            self.insert_node(key, val)

            return val
        else:
            return -1


    def put(self, key: int, value: int) -> None:

        if key in self.hashmap:

            # Remove and insert the node
            self.remove_node(key)
            self.insert_node(key, value)
        
        elif len(self.hashmap) < self.capacity:
            self.insert_node(key, value)
        
        else:
            node = self.tail.prev
            old_key, old_val = node.key, node.val
            self.remove_node(old_key)
            self.insert_node(key, value)
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)