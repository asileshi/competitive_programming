from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        outgoing = defaultdict(list)
        for first,second in prerequisites:
            outgoing[second].append(first)
            indegree[first]+=1
        safe = []
        for c in range(numCourses):
            if indegree[c] == 0:
                safe.append(c)
        taken = 0
        while safe:
            current = safe.pop()
            taken+=1
            for c in outgoing[current]:
                indegree[c]-=1
                if indegree[c] == 0:
                    safe.append(c)
        return taken == numCourses
            