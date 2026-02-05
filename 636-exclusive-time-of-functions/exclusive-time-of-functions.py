class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        execution_time = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            arr = log.split(":")
            if arr[1] == "start":
                if len(stack) > 0:
                    execution_time[stack[-1]] += int(arr[2]) - prev_time
                stack.append(int(arr[0]))
                prev_time = int(arr[2])
            else:
                execution_time[stack[-1]] += int(arr[2]) - prev_time + 1
                stack.pop()
                prev_time = int(arr[2]) + 1
        
        return execution_time


        