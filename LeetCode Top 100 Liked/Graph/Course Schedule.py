class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0
        
        while q:
            course = q.popleft()
            taken += 1
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return taken == numCourses
