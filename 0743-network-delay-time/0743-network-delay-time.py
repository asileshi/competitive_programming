class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a,b,c in times:
            graph[a].append((b,c))
        visited = set()
        dist = [inf]*(n+1)
        dist[0] = -1
        heap = [(0,k)]
        while heap:
            d,node = heapq.heappop(heap)
            visited.add(node)
            dist[node] = min(dist[node],d)
            for neg,cur in graph[node]:
                if neg in visited:
                    continue
                else:
                    heapq.heappush(heap,(cur+d,neg))
        return max(dist) if len(visited) == n else -1
            
        
        
                
                
        