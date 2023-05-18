class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        for i in range(len(graph)):
            if color[i] == -1:
                color[i] = 1;
                q = [i]
                while q:
                    cur = q.pop()
                    for conn in graph[cur]:
                        if color[conn] == -1:
                            color[conn] = 1-color[cur]
                            q.append(conn)
                        elif color[conn] == color[cur]:
                            return False
        
        return True