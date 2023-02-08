class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for pair in adjacentPairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        start = None
        for n in graph:
            if len(graph[n]) == 1:
                start = n
                break
        ans = []
        visited = set()
        
        
        def dfs(node):
            ans.append(node)
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)

                    
        dfs(start)
        return ans
        