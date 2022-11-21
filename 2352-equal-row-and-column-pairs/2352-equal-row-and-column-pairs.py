class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        x = {}
        for i in range(len(grid)):
            x[i] = grid[i]
        y = {}
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(grid[j][i])
            y[i] = temp
        ans = 0
        for i in x:
            for j in y:
                if x[i] == y[j]:
                    ans+=1
        return ans
            
        