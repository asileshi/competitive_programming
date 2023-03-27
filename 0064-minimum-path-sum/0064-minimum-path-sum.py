class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        table = [[inf for _ in range(len(grid[0]))] for _ in range(len(grid))]
        table[0][0] = grid[0][0]
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j]!=inf:
                    if i+1<len(table):
                        table[i+1][j] = min(table[i+1][j],table[i][j]+grid[i+1][j])
                    if j+1<len(table[0]):
                        table[i][j+1] = min(table[i][j+1],table[i][j]+grid[i][j+1])
        return table[-1][-1]