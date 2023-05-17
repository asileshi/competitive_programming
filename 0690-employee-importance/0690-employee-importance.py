"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = 0
        graph = defaultdict(list)
        for emp in employees:
            graph[emp.id] = [emp.importance,emp.subordinates]
        cur = [id]
        while cur:
            nxt = []
            for sub in cur:
                ans+=graph[sub][0]
                nxt+=graph[sub][1]
            cur = nxt
        return ans
                
            