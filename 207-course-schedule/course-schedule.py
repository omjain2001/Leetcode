from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegrees = [0]*numCourses

        for i in prerequisites:
            adj[i[0]].append(i[1])
            indegrees[i[1]] += 1
        
        queue = deque()
        for idx, count in enumerate(indegrees):
            if count == 0:
                queue.append(idx)
        
        total = 0
        while(len(queue) > 0):
            node = queue.popleft()
            total += 1
            for i in adj[node]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
        
        if len(queue) == 0 and total != numCourses:
            return False
        return True

            