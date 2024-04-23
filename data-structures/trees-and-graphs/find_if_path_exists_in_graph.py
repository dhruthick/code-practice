class Solution:
    '''
    EASY: 1971
    There is a bi-directional graph with n vertices, where each vertex 
    is labeled from 0 to n - 1 (inclusive). The edges in the graph are 
    represented as a 2D integer array edges, where each edges[i] = [ui, vi] 
    denotes a bi-directional edge between vertex ui and vertex vi. Every 
    vertex pair is connected by at most one edge, and no vertex has an edge 
    to itself.

    You want to determine if there is a valid path that exists from vertex 
    source to vertex destination.

    Given edges and the integers n, source, and destination, return true if 
    there is a valid path from source to destination, or false otherwise.
    '''
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = collections.defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        visited = set()
        visited.add(source)
        q = [source]

        while q:
            node = q.pop(0)
            if node == destination:
                return True
            for n in adj_list[node]:
                # mark as visited and then visit -  vice-versa did not work
                if n not in visited:
                    visited.add(n)
                    q.append(n)
        return False
                