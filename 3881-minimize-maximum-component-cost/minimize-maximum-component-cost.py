class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:

        def count_connected_components(threshold):
            modified_edges = [ele for ele in edges if ele[2] <= threshold]

            # create adjacency list
            adj = {}
            for i in range(n):
                adj[i] = []

            for e in modified_edges:
                adj[e[0]].append(e[1])
                adj[e[1]].append(e[0])
            
            
            visited = [False] * n

            # DFS Traversal
            def dfs(node):
                visited[node] = True

                for ele in adj[node]:
                    if not visited[ele]:
                        dfs(ele)
            
            count = 0
            for i in range(n):
                if not visited[i]:
                    count += 1
                    dfs(i)
            
            return count

        if not edges:
            return 0
        
        # Binary search
        l = 0
        r = max([ele[2] for ele in edges])
        while(l <= r):
            mid = (l+r) // 2

            count = count_connected_components(mid)
            if count <= k:
                r = mid - 1
            else:
                l = mid + 1
        
        return l

        