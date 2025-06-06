from collections import defaultdict, deque
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        INF = 1e10

        if len(flights) == 0:
            return -1

        adj = defaultdict(list)
        for i in flights:
            adj[i[0]].append(i[1:])


        q = deque([(0,src,0)])
        dist = [INF] * n
        dist[src] = 0

        while(len(q) > 0):
            stops, node, d = q.popleft()
            if stops > k:
                continue

            for ele in adj[node]:
                if ele[1] + d < dist[ele[0]]:
                    dist[ele[0]] = ele[1] + d
                    q.append((stops+1, ele[0], dist[ele[0]]))
        
        if dist[dst] == INF:
            return -1
        return dist[dst]