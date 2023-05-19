class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x,y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        color = [-1 for _ in range(n+1)]
        for i in range(1, n+1):
            if color[i]==-1:
                q = [i]
                color[i] = 1
                while q:
                    cur = q.pop()
                    for con in graph[cur]:
                        if color[con] == color[cur]:
                            return False
                        elif color[con] ==-1:
                            color[con] = 1-color[cur]
                            q.append(con)
        return True