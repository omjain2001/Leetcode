class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:

        # [(1,8),(2,10),(5,2),(11,3)]
        # [(1,9),(2,12),(5,7),(11,14)]
        # min(all_end_times) = 7

        mini = 1e10
        for t in tasks:
            mini = min(mini, t[0]+t[1])
        
        return mini
        