class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        ans = [False]
        color = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def valid(i,j):
            return 0<=i<len(grid) and 0<=j<len(grid[0])
        
        def dfs(parent,child):
            ci,cj = child
            color[ci][cj] = 1
            for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                newi,newj = ci+x,cj+y
                if (newi,newj) == parent or not valid(newi,newj):
                    continue
                if grid[newi][newj] == grid[ci][cj]:
                    if color[newi][newj] == 1:
                        ans[0] = True
                        return 
                    elif color[newi][newj] == 0:
                        dfs(child,(newi,newj))
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if color[i][j] == 0:
                    dfs((-1,-1),(i,j))
                    if ans[0] == True:
                        return True
        return False
                    