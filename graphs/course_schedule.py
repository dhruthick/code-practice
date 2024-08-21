class Solution:
    '''
    207: MEIDUM
    
    There are a total of numCourses courses you have 
    to take, labeled from 0 to numCourses - 1. You 
    are given an array prerequisites where 
    prerequisites[i] = [ai, bi] indicates that you 
    must take course bi first if you want to take 
    course ai.

    For example, the pair [0, 1], indicates that to 
    take course 0 you have to first take course 1.
    Return true if you can finish all courses. 
    Otherwise, return false.
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # need to detect if the graph is acyclic
        # time and space - O(m + n)
        # topological sorting using kahn's algorithm
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return nodesVisited == numCourses
    
        # # alternative dfs-based approach 
    
        # # build adj list
        # al = [[] for _ in range(numCourses)]
        # for s, f in prerequisites:
        #     al[s].append(f)
        # flag = True
        
        # # keep track of nodes in current dfs traversal
        # visited = set()
        # def dfs(crs):
        #     # loop detected
        #     if crs in visited:
        #         return False
        #     # no pre-reqs
        #     if al[crs] == []:
        #         return True
            
        #     visited.add(crs)
        #     # recursively explore each neighbouring path.
        #     for n in al[crs]:
        #         if not dfs(n): return False
        #     visited.remove(crs)
            
        #     # if we reach this in another dfs call, reduce computation 
        #     al[crs] = []

        #     return True

        # for i in range(numCourses):
        #     if not dfs(i): return False
        
        # return True 
