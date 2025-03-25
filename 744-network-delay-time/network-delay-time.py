from collections import defaultdict
from heapq import heapify, heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        if len(times) == 0:
            return 0
        
        adj = defaultdict(list)
        for time in times:
            adj[time[0]].append(time[1:])

        dist = [10**9] * (n+1)
        pq = []
        dist[k] = 0
        pq.append((dist[k],k))

        while(len(pq) > 0):
            node = heappop(pq)

            for i in adj[node[1]]:
                u = node[1]
                v = i[0]
                if dist[u] + i[1] < dist[v]:
                    dist[v] = dist[u] + i[1]
                    heappush(pq, (dist[v], v))
                
        if max(dist[1:]) == 10**9:
            return -1
        return max(dist[1:])

        