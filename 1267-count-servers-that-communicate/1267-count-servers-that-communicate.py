class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        x,y = defaultdict(int),defaultdict(int)
        computers = 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    computers+=1
                    x[i]+=1
                    y[j]+=1
                    if x[i] >= 2:
                        y[j] = 2
                    elif y[j] >= 2:
                        x[i] = 2
        notconnected = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    if x[i]<2 and y[j]<2:
                        notconnected+=1
        return computers-notconnected