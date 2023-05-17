class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        def dfs(graph,node):
            visited.add(node)
            if not graph[node]:
                return
            for i in graph[node]:
                if i not in visited:
                    dfs(graph,i)
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    graph[i+1].append(j+1)
                    graph[j+1].append(i+1)
        ans = 0
        for i in range(1,len(isConnected)+1):
            if i not in visited:
                ans+=1
                dfs(graph,i)
        return ans