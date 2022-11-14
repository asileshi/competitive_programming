class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[1],time[2]))
        heap = [(0,k)]
        ans = 0
        visited = set()
        while heap:
            w,c = heapq.heappop(heap)
            if c in visited:
                continue
            ans = max(ans,w)
            visited.add(c)
            for k,m in graph[c]:
                if k not in visited:
                    heapq.heappush(heap,(w+m,k))
        if len(visited) == n:
            return ans
        return -1
            
            
        