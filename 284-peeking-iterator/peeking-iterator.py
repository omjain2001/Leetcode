# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked_val = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked_val is None:
            if not self.iterator.hasNext():
                raise StopIteration()
            self.peeked_val = self.iterator.next()
        return self.peeked_val 
        

    def next(self):
        """
        :rtype: int
        """
        to_return = None
        if self.peeked_val is not None:
            to_return = self.peeked_val
            self.peeked_val = None
        
        if to_return:
            return to_return
        else:
            if not self.iterator.hasNext():
                raise StopIteration()
            return self.iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeked_val is not None or self.iterator.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].