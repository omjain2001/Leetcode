class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.par = [-1]*(n+1)

        for i in range(n+1):
            self.par[i] = i
    
    def findPar(self, node):
        if node == self.par[node]:
            return node
        self.par[node] = self.findPar(self.par[node])
        return self.par[node]
    
    def unionByRank(self, x, y):
        px = self.findPar(x)
        py = self.findPar(y)

        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.par[px] = py
        elif self.rank[py] < self.rank[px]:
            self.par[py] = px
        else:
            self.par[px] = py
            self.rank[py] += 1
        
        return True
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for e in edges:
            nodes.add(e[0])
            nodes.add(e[1])
        ds = DisjointSet(len(nodes))

        for e in edges:
            if not ds.unionByRank(e[0],e[1]):
                return e
        
        return []
        
        