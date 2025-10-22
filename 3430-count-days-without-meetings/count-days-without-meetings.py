class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        if len(meetings) == 0:
            return days
        
        meetings.sort(key=lambda x: [x[0],-x[1]])

        s = meetings[0][0]
        e = meetings[0][1]

        count = s-1
        idx = 0
        while(idx < len(meetings)):
            if meetings[idx][0] <= e:
                e = max(e, meetings[idx][1])
            else:
                count += meetings[idx][0]-e-1
                s = meetings[idx][0]
                e = meetings[idx][1]
            idx += 1
        count += (days-e)

        return count
        