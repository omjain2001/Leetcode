class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        ans = []
        idx = 0
        while(idx < len(intervals)-1):
            if intervals[idx][1] < intervals[idx+1][0]:
                ans.append(intervals[idx])
                idx += 1
            else:
                start = intervals[idx][0]
                end = intervals[idx][1]
                idx += 1
                while(idx < len(intervals) and end >= intervals[idx][0]):
                    end = max(end, intervals[idx][1])
                    idx += 1
                ans.append([start, end])
        
        if idx == len(intervals)-1:
            ans.append(intervals[idx])
        
        return ans

                
                
        
        