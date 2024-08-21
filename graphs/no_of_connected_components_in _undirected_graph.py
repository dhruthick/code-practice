class Solution(object):
    '''
    323: MEDIUM
    You have a graph of n nodes. You are given an 
    integer n and an array edges where 
    edges[i] = [ai, bi] indicates that there is 
    an edge between ai and bi in the graph.

    Return the number of connected components in 
    the graph.
    '''
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        # time and space - O(v + e)

        visited = set()

        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def bfs(root):
            q = [root]
            while q:
                node = q.pop(0)
                if node not in visited:
                    visited.add(node)
                    q.extend(adj_list[node])
        
        n_comp = 0
        for node in range(n):
            if node not in visited:
                n_comp += 1
                bfs(node)
        return n_comp