class Solution:
    def numBusesToDestination(self, routes: List[List[int]], s: int, t: int) -> int:
        graph,visited_stops,visited_buses = defaultdict(set),set(),set()
        q = deque([(s,0)])
        
        
        for i, r in enumerate(routes):
            for j in r:
                graph[j].add(i)
                
        
        while q:
            v, d = q.popleft()
            if v == t:
                return d
            if v in visited_stops: 
                continue
            visited_stops.add(v)
            for b in graph[v]:
                if b in visited_buses:
                    continue
                if t in routes[b]:
                    return d+1
                for w in routes[b]:
                    q.append((w,d+1))
                visited_buses.add(b)
                
                
        return -1