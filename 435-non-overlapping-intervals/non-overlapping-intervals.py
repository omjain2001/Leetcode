class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: [x[1], x[0]])
        # print(intervals)

        if len(intervals) == 0:
            return []
        
        start = intervals[0][0]
        end = intervals[0][1]
        idx = 1
        count = 0
        while(idx < len(intervals)):
            if end > intervals[idx][0]:
                # print(end, intervals[idx][0])
                count += 1
            else:
                start = intervals[idx][0]
                end = intervals[idx][1]
            
            idx += 1
        
        return count
            
            
        