class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ans = inf
        graph = defaultdict(list)
        for g in roads:
            graph[g[0]].append([g[1],g[-1]])
            graph[g[1]].append([g[0],g[-1]])
        visited = set()
        ans = inf
        def dfs(node):
            nonlocal ans
            if node in visited:
                return
            visited.add(node)
            for n in graph[node]:
                ans = min(n[-1],ans)
                dfs(n[0])
        dfs(1)
        return ans