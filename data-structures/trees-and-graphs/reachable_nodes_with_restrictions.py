class Solution(object):
    '''
    MEDIUM: 2368
    There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

    You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] 
    indicates that there is an edge between nodes ai and bi in the tree. You are also 
    given an integer array restricted which represents restricted nodes.

    Return the maximum number of nodes you can reach from node 0 without visiting a 
    restricted node.

    Note that node 0 will not be a restricted node.
    '''
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q = [0]
        visited = set(restricted)
        visited.add(0)
        ans = 0
        while q:
            node = q.pop(0)
            ans += 1
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    q.append(n)
        return ans

        