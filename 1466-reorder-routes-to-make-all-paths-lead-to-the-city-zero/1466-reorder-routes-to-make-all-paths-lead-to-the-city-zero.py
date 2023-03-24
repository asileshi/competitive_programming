class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
        possible = set([(x,y) for x,y in connections])
        ans = [0]
        def dfs(node):
            for n in graph[node]:
                if (node,n) not in visited:
                    visited.add((node,n))
                    visited.add((n,node))
                    if (n,node) in possible:
                        dfs(n)
                    else:
                        ans[0]+=1
                        dfs(n)
        dfs(0)
        return ans[0]