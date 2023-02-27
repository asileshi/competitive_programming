class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])
        cur = 0
        for task in tasks:
            cur = max(cur + task[0], task[1])
        return cur