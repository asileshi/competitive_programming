class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirr = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid)-1] == 1:
            return -1
        
        q = deque([(0, 0, 1)])
        
        
        while q:
            x, y, z = q.popleft()
            if x == y == len(grid)-1 :
                return z
            
            
            for di, dj in dirr :
                ni, nj = x+di, y+dj
                if 0<=ni<len(grid) and 0<=nj<len(grid) and grid[ni][nj] == 0:
                    q.append((ni, nj, z+1))
                    grid[ni][nj] = 1
                    
        return -1