from heapq import heapify, heappush, heappop
from collections import deque


class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * n
        self.par = [i for i in range(n)]
    
    def findPar(self, node):
        if self.par[node] == node:
            return node
        self.par[node] = self.findPar(self.par[node])
        return self.par[node]
    
    def unionByRank(self, node1, node2):
        par_node1 = self.findPar(node1)
        par_node2 = self.findPar(node2)

        # print(par_node1, par_node2)

        if par_node1 == par_node2:
            return False
        
        if self.rank[par_node1] < self.rank[par_node2]:
            self.par[par_node1] = par_node2
        elif self.rank[par_node1] > self.rank[par_node2]:
            self.par[par_node2] = par_node1
        else:
            self.par[par_node1] = par_node2
            self.rank[par_node2] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # Find the weights of all the edges
        # Put them in a priority queue
        # For each edge, check if the nodes are not already visited.
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1 = points[i][0]
                x2 = points[j][0]
                y1 = points[i][1]
                y2 = points[j][1]
                cost = abs(x1-x2) + abs(y1-y2)
                edges.append([cost, i, j])

        edges.sort(key = lambda x: x[0])
        edges = deque(edges)
        
        count = len(points) - 1
        ans = 0
        # print(edges)
        ds = DisjointSet(len(points))

        while(count > 0):
            node = edges.popleft()
            if ds.unionByRank(node[1], node[2]):
                # print(node)
                ans += node[0]
                count -= 1
            
        return ans