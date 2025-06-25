class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        if len(intervals) == 0:
            return []
        start = intervals[0][0]
        end = intervals[0][1]
        idx = 0
        ans = []
        while(idx < len(intervals)):
            # while(idx < len(intervals) and end >= intervals[idx][0]):
            #     end = max(end, intervals[idx][1])
            #     idx += 1
            # ans.append([start, end])
            # if idx < len(intervals):
            #     start = intervals[idx][0]
            #     end = intervals[idx][1]
            if intervals[idx][0] <= end:
                end = max(end, intervals[idx][1])
            else:
                ans.append([start, end])
                start = intervals[idx][0]
                end = intervals[idx][1]
            idx += 1
        
        ans.append([start, end])
        
        return ans
            
            
            
            
        