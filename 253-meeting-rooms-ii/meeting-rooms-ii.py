class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start = [time[0] for time in intervals]
        end = [time[1] for time in intervals]

        start.sort()
        end.sort()

        rooms = 0
        max_rooms = 0
        e = 0
        i = 0
        while(i < len(start)):
            if start[i] < end[e]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                i += 1
            else:
                rooms -= 1
                e += 1

        return max_rooms
        