class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(position[i], speed[i]) for i in range(len(position))]
        arr.sort()
        res = 0
        curr_time = 0
        for ele in range(len(position)-1, -1, -1):
            time = (target - arr[ele][0]) / arr[ele][1]
            if time > curr_time:
                res += 1
                curr_time = time
        
        return res