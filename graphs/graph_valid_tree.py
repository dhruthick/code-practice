class Solution(object):
    '''
    261: MEDIUM
    
    You have a graph of n nodes labeled from 
    0 to n - 1. You are given an integer n 
    and a list of edges where 
    edges[i] = [ai, bi] indicates that there 
    is an undirected edge between nodes ai 
    and bi in the graph.

    Return true if the edges of the given 
    graph make up a valid tree, and false 
    otherwise.
    '''
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        from collections import defaultdict
        # time and space - O(v + e)
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set() # to check connectivity
        tracked = set() # to check for cycles
        def dfs(node):
            # loop detected
            if node not in visited: visited.add(node)
            if node in tracked:
                return False
            # no pre-reqs
            if not adj_list[node]:
                return True
            
            tracked.add(node)
            # recursively explore each neighbouting path.
            for n in adj_list[node]:
                # extra condition because the graph is undirected
                if node in adj_list[n]: 
                    adj_list[n].remove(node)
                if not dfs(n): 
                    return False
            tracked.remove(node)

            return True

        return dfs(0) and len(visited) == n