class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.num_elements = 0
        self.queue = [0] * k
        self.front = -1
        self.rear = -1
        

    def enQueue(self, value: int) -> bool:
        # Check if queue is full
        if self.num_elements == self.size:
            return False
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.num_elements += 1

        if self.front == -1:
            self.front = (self.front + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.num_elements == 0:
            return False
        
        self.num_elements -= 1
        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.num_elements == 0:
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.num_elements == 0:
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.num_elements == 0

    def isFull(self) -> bool:
        return self.num_elements == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()