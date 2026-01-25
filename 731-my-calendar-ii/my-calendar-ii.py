class MyCalendarTwo:

    def __init__(self):
        self.start = []
        self.end = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        
        start = [ele for ele in self.start]
        end = [ele for ele in self.end]
        start.append(startTime)
        end.append(endTime)

        start.sort()
        end.sort()

        i = 0
        count = 0
        max_count = 0
        e = 0
        while(i < len(start)):
            if start[i] < end[e]:
                count += 1
                max_count = max(max_count, count)
                i += 1
            else:
                count -= 1
                e += 1
        
        if max_count > 2:
            return False
        else:
            self.start.append(startTime)
            self.end.append(endTime)
            return True
        
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)